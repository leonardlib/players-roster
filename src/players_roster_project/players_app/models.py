from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        permissions = [
            ('list_all_teams', 'Can list all teams'),
            ('list_team', 'Can list single team'),
        ]

    def __str__(self):
        """
        Get the representational string from Team
        :author: @leonard_lib
        :date: 2020-08-31
        :return: string
        """
        return self.name


class Player(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    jersey_number = models.PositiveIntegerField(blank=False)
    team = models.ForeignKey(
        Team,
        related_name="team",
        on_delete=models.CASCADE,
        default=None
    )

    def full_name(self):
        """
        Get the full name from Player
        :author: @leonard_lib
        :date: 2020-08-31
        :return: string
        """
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        """
        Get the representational string from Player
        :author: @leonard_lib
        :date: 2020-08-31
        :return: string
        """
        return self.first_name
