import graphene

from .schema import UserType
from ..models import User


class CreateUserMutation(graphene.Mutation):
    """
    GraphQL mutation to create a User
    :author: @leonard_lib
    :date: 2020-09-01
    """
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, password):
        email = email.lower()
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        return CreateUserMutation(user=user)


class UsersAppMutations(graphene.ObjectType):
    """
    All users app mutations to export
    :author: @leonard_lib
    :date: 2020-09-01
    """
    create_user = CreateUserMutation.Field()
