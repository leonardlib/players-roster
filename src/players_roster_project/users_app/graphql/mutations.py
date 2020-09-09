import graphene
from django.contrib.auth.models import Group, Permission

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


class CreateUserGroupMutation(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        name = name.lower()
        Group.objects.create(name=name)
        return CreateUserGroupMutation(success=True)


class AddPermissionToGroupMutation(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        group_name = graphene.String(required=True)
        permission_name = graphene.String(required=True)

    def mutate(self, info, group_name, permission_name):
        group_name = group_name.lower()
        permission_name = permission_name.lower()
        group = Group.objects.get(name=group_name)
        permission = Permission.objects.get(codename=permission_name)
        group.permissions.add(permission)
        return AddPermissionToGroupMutation(success=True)


class AddUserToGroupMutation(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String(required=True)
        group_name = graphene.String(required=True)

    def mutate(self, info, email, group_name):
        group_name = group_name.lower()
        email = email.lower()
        group = Group.objects.get(name=group_name)
        user = User.objects.get(email=email)
        group.user_set.add(user)
        return AddUserToGroupMutation(success=True)


class UsersAppMutations(graphene.ObjectType):
    """
    All users app mutations to export
    :author: @leonard_lib
    :date: 2020-09-01
    """
    create_user = CreateUserMutation.Field()
    create_user_group = CreateUserGroupMutation.Field()
    add_perm_to_group = AddPermissionToGroupMutation.Field()
    add_user_to_group = AddUserToGroupMutation.Field()
