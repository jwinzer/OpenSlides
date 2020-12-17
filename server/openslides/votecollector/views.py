import base64
import hashlib
import hmac
import json

from django.db import transaction
from django.db.utils import IntegrityError
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from ..core.config import config
from ..motions.views import MotionPoll, MotionPollViewSet
from ..poll.views import BasePoll
from ..users.models import User
from ..utils.auth import in_some_groups
from ..utils.autoupdate import inform_changed_data
from ..utils.rest_api import ErrorLoggingMixin


def authenticate(body):
    """
    Authenticates and decodes the VoteCollector message body. Uses HMAC authentication.
    :param body: json dictionary with keys "message" and "hmac"
    :return: decoded data
    """
    if isinstance(body, bytes):
        body = body.decode("utf-8")
    try:
        d = json.loads(body)

        # Create HMAC hash of the message.
        key = bytes(settings.SECRET_KEY, "utf-8")
        digest = hmac.new(key, bytes(d["message"], "utf-8"), hashlib.sha256).digest()
        hmac_hash = base64.b64encode(digest).decode("utf-8")
        
        # Hash must match the hmac value sent.
        if hmac_hash != d["hmac"]:
            raise ValidationError({"detail": "HMAC authentication has failed."})
        return json.loads(d["message"])
    except (ValueError, TypeError, KeyError):
        raise ValidationError({"detail": "Request content is malformed."})


def validate_data(data):
    """
    Validates VoteCollector data.
    :param data: decoded data
    :return: votes list
    """
    votes = data if isinstance(data, list) else [data]
    for vote in votes:
        if not isinstance(vote, dict):
            raise ValidationError({'detail': 'All votes have to be a dict.'})
        if 'value' not in vote:
            raise ValidationError({'detail': 'A vote value is missing.'})
        if 'id' not in vote or not isinstance(vote["id"], int):
            raise ValidationError({'detail': 'id is missing or invalid.'})
    return votes


def validate_yna_votes(votes):
    for vote in votes:
        value = vote["value"]
        if value not in ("Y", "N", "A"):
            raise ValidationError({"detail": "Value must be Y, N or A."})


class VoteCollectorVoteViewSet(ErrorLoggingMixin, APIView):
    authentication_classes = []

    @transaction.atomic
    def post(self, request, poll_id):
        # Validate VoteCollector enabled.
        if not config["voting_enable_votecollector"]:
            raise ValidationError({"detail": "VoteCollector not enabled."})

        # Validate motion poll state and type.
        poll_id = int(poll_id)
        try:
            poll = MotionPoll.objects.get(id=poll_id)
        except MotionPoll.DoesNotExist:
            raise ValidationError({"detail": "Motion poll does not exist."})
        if poll.state != BasePoll.STATE_STARTED:
            raise ValidationError({"detail": "Poll has not started."})
        if poll.type == BasePoll.TYPE_ANALOG:
            raise ValidationError({"detail": "Poll type is analog."})

        # Authenticate and validate VoteCollector data.
        data = authenticate(request.body)
        votes = validate_data(data)
        validate_yna_votes(votes)

        # Create motion votes.
        poll_groups = list(poll.groups.values_list("pk", flat=True))
        motion_poll_view_set = MotionPollViewSet()
        for vote in votes:
            # Get request user (active voter) and validate presence.
            try:
                request_user = get_user_model().objects.get(keypad=vote["id"])
            except User.DoesNotExist:
                continue
            if not request_user.is_present:
                continue

            # Get all vote users (request user and delegated from users).
            vote_users = [request_user] + list(request_user.vote_delegated_from_users.all())
            for vote_user in vote_users:
                if not in_some_groups(vote_user.id, poll_groups, exact=True):
                    # User does not belong to a poll group.
                    continue
                try:
                    motion_poll_view_set.add_user_to_voted_array(vote_user, poll)
                except IntegrityError:
                    # User has already voted. Vote is ignored.
                    continue
                motion_poll_view_set.handle_named_vote(vote["value"], poll, vote_user, request_user)

        inform_changed_data(poll)
        return Response()
