from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from shortener.services import base62_encode
from .models import ShortLink, default_expiration
from shortener.serializer import ShortLinkSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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
        # pega o objeto pelo ID
        link = get_object_or_404(ShortLink, pk=pk)

        # gera o código curto
        combined = (str(pk) + link.original_link).encode("utf-8")
        surl = base62_encode(combined)[:6]

        # salva no objeto
        link.shorted_link = surl
        link.expires_at = default_expiration()
        link.save()

        return JsonResponse({"surl": surl})
