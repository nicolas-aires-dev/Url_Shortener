from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from shortener.services import generate_short_url
from shortener.models import ShortLink
from shortener.serializer import ShortLinkSerializer


class ShortLinkCreateListView(generics.ListCreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer

class ShortlinkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer

class GenerateSurlView(View):
    def get(self, request, pk):
        obj = get_object_or_404(ShortLink, pk=pk)
        surl = generate_short_url(obj)
        return JsonResponse(surl)