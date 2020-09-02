import graphene

from graphene_django import DjangoListField
from graphql_jwt.decorators import login_required

from ..graphql.schema import UserType
from ..models import User


class UsersAppQueries(graphene.ObjectType):
    """
    GraphQL queries for users app
    :author: @leonard_lib
    :date: 2020-09-01
    """
    all_users = DjangoListField(UserType)
    user_by_id = graphene.Field(
        UserType,
        id=graphene.ID(required=True)
    )
    user_by_email = graphene.Field(
        UserType,
        email=graphene.String(required=True)
    )

    @login_required
    def resolve_all_users(self, info):
        """
        Get all users
        :author: @leonard_lib
        :date: 2020-09-01
        :param info:
        :return List of User:
        """
        print(info.context.user)
        return User.objects.all()

    @login_required
    def resolve_user_by_id(self, info, id):
        """
        Get player by ID
        :author: @leonard_lib
        :date: 2020-09-01
        :param info:
        :param id:
        :return:
        """
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    @login_required
    def resolve_user_by_email(self, info, email):
        """
        Get player by email
        :author: @leonard_lib
        :date: 2020-09-01
        :param info:
        :param email:
        :return:
        """
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
