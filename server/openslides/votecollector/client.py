from xmlrpc.client import Error, ServerProxy

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_noop

from openslides.core.config import config


VOTECOLLECTOR_ERROR_MESSAGES = {
    -1: ugettext_noop("Unknown voting mode."),
    -2: ugettext_noop("Invalid keypad range."),
    -3: ugettext_noop("Invalid keypad list."),
    -4: ugettext_noop("No keypads authorized for voting."),
    -5: ugettext_noop("License not sufficient."),
    -6: ugettext_noop("No voting device connected."),
    -7: ugettext_noop("Failed to set up voting device."),
    -8: ugettext_noop("Voting device not ready."),
    -9: ugettext_noop("Voting device not licensed."),
}


class VoteCollectorError(Exception):
    """
    Error class for the VoteCollector.
    """
    def __init__(self, value=None, nr=None):
        if nr is not None:
            self.value = _(VOTECOLLECTOR_ERROR_MESSAGES[nr])
        elif value is not None:
            self.value = value
        else:
            self.value = _("No connection to VoteCollector.")

    def __str__(self):
        return repr("VoteCollector Exception: %s" % self.value)


def get_callback_url(request):
    return request.META["HTTP_ORIGIN"] + "/votecollector"


class Client:
    """
    VoteCollector client.
    """
    def __init__(self, uri="http://localhost:8030"):
        try:
            self._server = ServerProxy(uri)
        except OSError as e:
            raise VoteCollectorError(str(e))

    def get_device_status(self):
        try:
            status = self._server.voteCollector.getDeviceStatus()
        except (IOError, Error):
            raise VoteCollectorError()
        return status

    def start_voting(self, mode, callback_url, options=None):
        keypads = get_user_model().objects.filter(is_present=True, keypad__isnull=False).values_list(
            "keypad", flat=True).order_by("keypad")
        if not keypads:
            raise VoteCollectorError(_("No keypads exists for active users."))

        # Call getDeviceStatus to verify VoteCollector is configured with a secret key.
        try:
            status = self._server.voteCollector.getDeviceStatus()
        except (IOError, Error):
            raise VoteCollectorError(_("No connection to VoteCollector."))
        if "Secret Key: Yes" not in status:
            raise VoteCollectorError(_("VoteCollector does not use a secret key."))

        # Call prepareVoting.
        ext_mode = options + ";" + callback_url if options else callback_url
        try:
            count = self._server.voteCollector.prepareVoting(mode + "-" + ext_mode, 0, 0, list(keypads))
        except (IOError, Error):
            raise VoteCollectorError()
        if count < 0:
            raise VoteCollectorError(nr=count)

        # Call startVoting.
        import time
        time.sleep(2)
        try:
            count = self._server.voteCollector.startVoting()
        except (IOError, Error):
            raise VoteCollectorError()
        if count < 0:
            raise VoteCollectorError(nr=count)

        return count, status

    def stop_voting(self):
        try:
            self._server.voteCollector.stopVoting()
        except (IOError, Error):
            raise VoteCollectorError()
        return True

    def get_voting_status(self):
        """
        Returns voting status as a list: [elapsed_seconds, votes_received]
        """
        try:
            status = self._server.voteCollector.getVotingStatus()
        except (IOError, Error):
            raise VoteCollectorError()
        return status

    def get_voting_result(self):
        """
        Returns the voting result as a list.
        """
        try:
            result = self._server.voteCollector.getVotingResult()
        except (IOError, Error):
            raise VoteCollectorError()
        return result
