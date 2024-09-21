from uuid import uuid4

from django.db import transaction

from Stadium.dao.seat_dao import SeatDao
from Stadium.dao.stadium_dao import StadiumDao
from Stadium.models import Seat


class StadiumLogic:
    def __init__(self):
        self.stadium_dao = StadiumDao()
        self.seat_dao = SeatDao()

    def add_stadium(
            self,
            potential,
            address,
            name,
    ):
        with transaction.atomic():
            stadium = self.stadium_dao.add_stadium(
                potential=potential,
                address=address,
                name=name, )
            seats_obj = [Seat(code=uuid4(), stadium=stadium) for _ in range(0, potential)]
            seats = self.seat_dao.add_bulk_seats(seats_obj=seats_obj)

    def get_all_stadiums(self):
        stadiums = self.stadium_dao.get_all_stadiums()
        stadiums_dict = [{
            "name": stadium.name,
            "potential": stadium.potential,
            "address": stadium.address
        } for stadium in stadiums]
        return stadiums_dict
