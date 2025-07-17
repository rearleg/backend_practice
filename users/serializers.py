from rest_framework import serializers
from .models import User
from tweets.serializers import TweetSerializer


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    username = serializers.CharField(
        max_length=100,
        required=True,
    )
    tweets = TweetSerializer(
        many=True,
    )