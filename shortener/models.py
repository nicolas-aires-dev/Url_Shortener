from django.db import models
from django.utils import timezone
from datetime import timedelta

class ShortLink(models.Model):
    link_title = models.CharField(null=False, blank=False, max_length=100)
    created_at = models.DateField(auto_now_add=True)
    expires_at = models.DateField(default=lambda: timezone.now() + timedelta(days=5))
    original_link = models.CharField(null=False, blank=False, max_length=200)
    clicks = models.IntegerField(default=0)