from django.db import models
from django.utils import timezone
from datetime import timedelta


def default_expiration():
    return timezone.now().date() + timedelta(days=5)

class ShortLink(models.Model):
    link_title = models.CharField(null=False, blank=False, max_length=100)
    created_at = models.DateField(auto_now_add=True)
    expires_at = models.DateField(default=default_expiration)
    original_link = models.CharField(null=False, blank=False, max_length=200)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.link_title
