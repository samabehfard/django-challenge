from Stadium.models import Seat


class SeatDao:
    def add_bulk_seats(self, seats_obj):
        Seat.objects.bulk_create(seats_obj)
    def seat_codes_count_exist_in_stadium(self,seats_code,stadium):
        return Seat.objects.filter(stadium=stadium,seat_code__in=seats_code).count()
