from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        """
        String representation of User
        :return:
        """
        return self.email
