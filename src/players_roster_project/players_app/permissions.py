from django_graphene_permissions.permissions import BasePermission


class ListPlayersPermission(BasePermission):
    @staticmethod
    def has_permission(context):
        return context.user and context.user.is_staff

    @staticmethod
    def has_object_permission(context, obj):
        return True
