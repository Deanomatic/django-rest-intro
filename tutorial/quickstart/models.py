from django.db import models

class FootballTeam(models.Model):
    team_name = models.CharField(max_length=30)
    team_ranking = models.CharField(max_length=30)
    roster = models.IntegerField()
    coach = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

