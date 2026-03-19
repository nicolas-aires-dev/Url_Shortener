from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from shortener.serializer import ShortLinkSerializer
from .models import ShortLink, default_expiration
from django.shortcuts import get_object_or_404, redirect
from shortener.services import base62_encode
from django.utils import timezone
from rest_framework import generics
from django.http import JsonResponse
from django.views import View


@method_decorator(csrf_exempt, name='dispatch')
class ShortLinkCreateListView(generics.ListCreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ShortlinkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer

@method_decorator(csrf_exempt, name='dispatch')
class GenerateSurlView(View):
    def get(self, request, pk):
        # selects object by ID
        link = get_object_or_404(ShortLink, pk=pk)

        # generate short code
        combined = (str(pk) + link.original_link).encode("utf-8")
        surl = base62_encode(combined)[:6]

        # saves object
        link.shorted_link = surl
        link.surl_expires_at = default_expiration()
        link.surl_created_at = timezone.now().date()
        link.save()

        return JsonResponse({"surl": surl, "surl_expires_at": link.surl_expires_at, "surl_created_at": link.surl_created_at})
