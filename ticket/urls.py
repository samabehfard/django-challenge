from django.urls import path

from ticket.api.controller.tickets_list_controller import TicketListView

urlpatterns = [
    path('buy_ticket/', TicketListView.as_view(), name='buy_ticket'),
]
