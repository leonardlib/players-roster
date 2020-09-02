import graphene
import graphql_jwt

from .players_app.graphql.mutations import PlayersAppMutations
from .players_app.graphql.queries import PlayersAppQueries
from .users_app.graphql.mutations import UsersAppMutations
from .users_app.graphql.queries import UsersAppQueries


class Queries(
    PlayersAppQueries,
    UsersAppQueries,
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
    UsersAppMutations,
    graphene.ObjectType
):
    """
    All mutations for GraphQL Schema
    :author: @leonard_lib
    :date: 2020-09-01
    """
    auth_token = graphql_jwt.ObtainJSONWebToken().Field()


schema = graphene.Schema(query=Queries, mutation=Mutations)
