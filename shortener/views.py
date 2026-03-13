from rest_framework import generics
from shortener.models import ShortLink

class ShortLinkCreateListView(generics.ListCreateAPIView):
    queryset = ShortLink.objects.all