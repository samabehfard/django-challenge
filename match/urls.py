from django.urls import path

from match.api.controller.match_creation_controller import MatchView

urlpatterns = [
    path('match_list/', MatchView.as_view(), name='match_list'),
]
