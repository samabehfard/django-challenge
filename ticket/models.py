from django.contrib.auth.models import User
from django.db import models

from Stadium.models import Seat
from match.models import Match


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    buy_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.user} - {self.seat}"
