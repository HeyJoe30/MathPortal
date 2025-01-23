from django.db import models
from django.conf import settings
from django.utils import timezone


class Publication(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='publication_created',
        on_delete=models.CASCADE
    )


    title = models.CharField()
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    class Meta:
        indexes = [
            models.Index(fields=['-publish']),
        ]
        ordering = ['-publish']

    def __str__(self):
        return self.title