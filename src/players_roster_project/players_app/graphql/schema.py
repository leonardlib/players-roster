import graphene

from graphene_django import DjangoObjectType
from ..models import Team, Player


class TeamType(DjangoObjectType):
    """
    Team type for GraphQL Schema
    :author: @leonard_lib
    :date: 2020-09-01
    """
    class Meta:
        model = Team
        fields = '__all__'


class PlayerType(DjangoObjectType):
    """
    Player type for GraphQL Schema
    :author: @leonard_lib
    :date: 2020-09-01
    """
    full_name = graphene.String()

    class Meta:
        model = Player
        fields = '__all__'

    def resolve_full_name(self, info):
        return self.full_name()
