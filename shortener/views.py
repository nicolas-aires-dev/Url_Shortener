from rest_framework import generics
from shortener.models import ShortLink
from shortener.serializers import ShortLinkSerializer


class ShortLinkCreateListView(generics.ListCreateAPIView):
    queryset = ShortLink.objects.all
    serializer_class = ShortLinkSerializer
