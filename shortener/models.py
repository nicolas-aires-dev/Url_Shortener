from django.db.models.signals import post_save
from shortener.models import ShortLink
from django.dispatch import receiver
from django.db import models
from django.utils import timezone
from datetime import timedelta


def default_expiration():
    return timezone.now().date() + timedelta(days=5)


class ShortLink(models.Model):
    link_title = models.CharField(null=False, blank=False, max_length=100)
    created_at = models.DateField(auto_now_add=True)
    surl_created_at = models.DateField(null=True, blank=True)
    surl_expires_at = models.DateField(default=default_expiration)
    original_link = models.CharField(null=False, blank=False, max_length=200)
    shorted_link = models.CharField(null=True, blank=True, max_length=200)
    clicks = models.IntegerField(default=0)

    @receiver(post_save, sender=ShortLink)
    def set_surl_created_at(sender, instance, created, **kwargs):
        if created and instance.shorted_link and not instance.surl_created_at:
            instance.surl_created_at = timezone.now().date()
            instance.save()

    def __str__(self):
        return self.link_title
