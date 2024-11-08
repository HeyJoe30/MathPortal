from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('regular', 'Обычный пользователь'),
        # ('moderator', 'Модератор'),
        # ('researcher', 'Исследователь'),
        # ('student', 'Студент'),
    )

    user_type = models.CharField(max_length=20,
                                 choices=USER_TYPE_CHOICES,
                                 default='regular')

    # def is_moderator(self):
    #     return self.user_type == 'moderator'
