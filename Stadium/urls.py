from django.urls import path

from Stadium.api.controller.stadium_list_controller import StadiumListView

urlpatterns = [
    path('stadium_list/', StadiumListView.as_view(), name='stadiums'),
]
