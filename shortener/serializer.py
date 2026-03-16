from rest_framework import serializers
from shortener.models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortLink
        fields= '__all__'
