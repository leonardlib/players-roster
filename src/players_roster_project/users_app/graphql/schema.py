from graphene_django import DjangoObjectType
from ..models import User


class UserType(DjangoObjectType):
    """
    User type for GraphQL Schema
    :author: @leonard_lib
    :date: 2020-09-01
    """
    class Meta:
        model = User
        exclude = [
            'password'
        ]
