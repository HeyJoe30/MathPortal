from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )

    date_of_birth = models.DateField(blank=True, null=True)

    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True
    )

    # USER_TYPE_CHOICES = (
    #     ('regular', 'Обычный пользователь'),
    #     # ('moderator', 'Модератор'),
    #     # ('researcher', 'Исследователь'),
    #     # ('student', 'Студент'),
    # )
    #
    # user_type = models.CharField(max_length=20,
    #                              choices=USER_TYPE_CHOICES,
    #                              default='regular')

    def __str__(self):
        return f'Profile of {self.user.username}'
