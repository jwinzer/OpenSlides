from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^vote/(?P<poll_id>\d+)/$", views.VoteCollectorVoteViewSet.as_view()),
]
