from django.db import models
from django.conf import settings


class Profile(models.Model):
    # We force the deletion of the related Profile object when a User object gets deleted.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    # It is possible to add more fields here
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

