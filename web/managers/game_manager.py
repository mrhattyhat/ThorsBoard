from django.db import models


class GameManager(models.Manager):

    def by_opp_and_season(self, team, opp, season):
        try:
            g = self.get_queryset().filter(
                ((models.Q(team1__id=team.id) & models.Q(team2__id=opp.id)) |
                (models.Q(team1__id=opp.id) & models.Q(team2__id=team.id))),
                season__id=season.id
            )[0]
            return g
        except IndexError:
            return None