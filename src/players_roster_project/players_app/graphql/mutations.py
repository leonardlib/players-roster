import graphene

from django import forms
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_jwt.decorators import login_required

from .schema import TeamType, PlayerType
from ..models import Team, Player


class TeamForm(forms.ModelForm):
    """
    Form parameters to create or update a Team
    :author: @leonard_lib
    :date: 2020-09-01
    """
    id = forms.IntegerField(required=False)

    class Meta:
        model = Team
        exclude = [
            'id'
        ]


class PlayerForm(forms.ModelForm):
    """
    Form parameters to create or update a Player
    :author: @leonard_lib
    :date: 2020-09-01
    """
    id = forms.IntegerField(required=False)

    class Meta:
        model = Player
        exclude = [
            'id'
        ]


class CreateOrUpdateTeamMutation(DjangoModelFormMutation):
    """
    GraphQL mutation to create or update a Team
    :author: @leonard_lib
    :date: 2020-09-01
    """
    team = graphene.Field(TeamType)

    class Meta:
        form_class = TeamForm


class CreateOrUpdatePlayerMutation(DjangoModelFormMutation):
    """
    GraphQL mutation to create or update a Player
    :author: @leonard_lib
    :date: 2020-09-01
    """
    player = graphene.Field(PlayerType)

    class Meta:
        form_class = PlayerForm


class RemoveTeamMutation(graphene.Mutation):
    """
    GraphQL mutation to delete a Team
    :author: @leonard_lib
    :date: 2020-09-01
    """
    removed = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    @login_required
    def mutate(self, info, id):
        team = Team.objects.get(pk=id)
        team.delete()
        return RemoveTeamMutation(removed=True)


class RemovePlayerMutation(graphene.Mutation):
    """
    GraphQL mutation to delete a Player
    :author: @leonard_lib
    :date: 2020-09-01
    """
    removed = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    @login_required
    def mutate(self, info, id):
        player = Player.objects.get(pk=id)
        player.delete()
        return RemovePlayerMutation(removed=True)


class PlayersAppMutations(graphene.ObjectType):
    """
    All players app mutations to export
    :author: @leonard_lib
    :date: 2020-09-01
    """
    create_or_update_team = CreateOrUpdateTeamMutation.Field()
    remove_team = RemoveTeamMutation.Field()
    create_or_update_player = CreateOrUpdatePlayerMutation.Field()
    remove_player = RemovePlayerMutation.Field()
