import graphene

from graphene_django import DjangoListField
from graphql_jwt.decorators import login_required

from ..graphql.schema import TeamType, PlayerType
from ..models import Player


class PlayersAppQueries(graphene.ObjectType):
    """
    GraphQL queries for players app
    :author: @leonard_lib
    :date: 2020-09-01
    """
    all_teams = DjangoListField(TeamType)
    all_players = graphene.List(PlayerType)
    all_players_for_team = graphene.List(
        PlayerType,
        team=graphene.ID(required=True)
    )
    player_by_last_name = graphene.Field(
        PlayerType,
        last_name=graphene.String(required=True)
    )

    @login_required
    def resolve_all_players(self, info):
        """
        Get all players
        :author: @leonard_lib
        :date: 2020-09-01
        :param info:
        :return List of Player:
        """
        return Player.objects.select_related('team').all()

    @login_required
    def resolve_all_players_for_team(self, info, team):
        """
        Get all players for a team
        :author: @leonard_lib
        :date: 2020-09-01
        :param info:
        :param team:
        :return List of Player:
        """
        return Player.objects.select_related('team').filter(team=team)

    @login_required
    def resolve_player_by_last_name(self, info, last_name):
        """
        Get player by last name
        :author: @leonard_lib
        :date: 2020-09-01
        :param info:
        :param last_name:
        :return:
        """
        try:
            return Player.objects.select_related('team').get(last_name=last_name)
        except Player.DoesNotExist:
            return None