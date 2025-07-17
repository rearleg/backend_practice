from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    payload = serializers.CharField(
        required=True,
    )

