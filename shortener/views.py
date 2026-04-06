from django.shortcuts import get_object_or_404, redirect
from settings.permissions import GlobalDefaultPermission
from rest_framework.permissions import IsAuthenticated
from shortener.serializer import ShortLinkSerializer
from .models import ShortLink, default_expiration
from shortener.services import base62_encode
from shortener.tasks import update_clicks
from django.http import JsonResponse
from rest_framework import generics
from django.utils import timezone
from django.views import View


class ShortLinkCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer


class ShortlinkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer


class GenerateSurlView(View):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)

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


class RedirectLink(View):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)

    def get(self, request, shorted_link):
        link = get_object_or_404(ShortLink, shorted_link=shorted_link)

        # Trigger async task
        update_clicks.delay(link.id)

        # Verify link expiration
        if link.surl_expires_at and timezone.now().date() > link.surl_expires_at:
            return JsonResponse({"error": "This link is expired or doesn't exist."}, status=410)

        return redirect(link.original_link)
