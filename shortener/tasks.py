from celery import shared_task
from shortener.models import ShortLink


@shared_task
def update_clicks(link_id):
    link = ShortLink.objects.get(id=link_id)
    link.clicks += 1
    link.save()
