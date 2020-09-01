import graphene

from .players_app.graphql.mutations import PlayersAppMutations
from .players_app.graphql.queries import PlayersAppQueries


class Queries(
    PlayersAppQueries,
    graphene.ObjectType
):
    """
    All queries for GraphQL Schema
    :author: @leonard_lib
    :date: 2020-09-01
    """
    pass


class Mutations(
    PlayersAppMutations,
    graphene.ObjectType
):
    """
    All mutations for GraphQL Schema
    :author: @leonard_lib
    :date: 2020-09-01
    """
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
