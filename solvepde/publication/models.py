from django.db import models
from django.conf import settings


class Publication(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='publication_created',
        on_delete=models.CASCADE
    )
    title = models.CharField()
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title