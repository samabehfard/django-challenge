from django.db import transaction

from ticket.adapter.buying_ticket import TicketBuyCenter
from ticket.dao.ticket_dao import TicketDao
from ticket.errors import ThereIsOccupiedSeatException, TicketsNotPaidException
from ticket.models import Ticket


class TicketLogic:
    def __init__(self):
        self.ticket_dao = TicketDao()
        self.ticket_adapter = TicketBuyCenter()

    def buy_ticket(
            self,
            seat_codes,
            match_id,
            user,
    ):
        with transaction.atomic():
            if self.ticket_dao.is_at_least_one_seat_occupied(seat_codes, match_id):
                raise ThereIsOccupiedSeatException("at least one of seats occupied")
            else:
                tickets = [
                    Ticket(user=user, match_id=match_id, seat_code=seat_code)
                    for seat_code in seat_codes]
                tickets = self.ticket_dao.create_bulk_tickets(tickets)
                result = self.ticket_adapter.pay_ticket()
                if result:
                    return tickets
                else:
                    self.ticket_dao.get_back_tickets(match_id, seat_codes)
                    raise TicketsNotPaidException("paid was unsuccessful")
        ticket_codes = [f"{seat_code}{match_id}" for seat_code in seat_codes]
        return ticket_codes
