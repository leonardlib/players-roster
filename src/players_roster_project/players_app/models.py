from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)

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

    def jersey_name(self):
        """
        Get the jersey name from Player
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
