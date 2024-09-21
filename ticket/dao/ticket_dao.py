from ticket.models import Ticket


class TicketDao:
    def create_bulk_tickets(self, tickets):
        Ticket.objects.bulk_create(tickets, ignore_conflicts=False)

    def is_at_least_one_seat_occupied(self, seat_codes, match_id):
        return Ticket.objects.filter(match_id=match_id, seat__code__in=seat_codes).all()

    def get_back_tickets(self, seat_codes, match_id):
        Ticket.objects.filter(match_id=match_id, seat__code__in=seat_codes).delete()
