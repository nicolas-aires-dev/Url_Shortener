from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from shortener.services import base62_encode
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
        link = get_object_or_404(ShortLink, pk=pk)
        combined = (str(pk) + link.original_link).encode("utf-8")
        surl = base62_encode(combined)[:6]
        return JsonResponse({"surl": surl})
