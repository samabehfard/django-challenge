from Stadium.models import Seat


class SeatDao:
    def add_bulk_seats(self, seats_obj):
        Seat.objects.bulk_create(seats_obj)
