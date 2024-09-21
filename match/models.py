from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    flag_image = models.ImageField(upload_to='team_flags/')

    def __str__(self):
        return self.name


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    default_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"

