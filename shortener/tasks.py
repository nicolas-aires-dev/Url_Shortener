from celery import shared_task
from shortener.models import ShortLink
from django.shortcuts import get_object_or_404


@shared_task
def update_clicks(clicks):
    surl_clicks = get_object_or_404(ShortLink, clicks=clicks)
    surl_clicks.clicks += 1
    surl_clicks.save()
