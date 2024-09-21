from django.db import models

from Stadium.models import Stadium


class Match(models.Model):
    home_matches = models.CharField()
    away_matches = models.CharField()
    date = models.DateField()
    time = models.TimeField()
    default_price = models.DecimalField(max_digits=10, decimal_places=2)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.home_matches} vs {self.away_matches} on {self.date}"

