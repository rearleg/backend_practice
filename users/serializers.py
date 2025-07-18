from rest_framework.serializers import ModelSerializer
from .models import User
from tweets.serializers import TweetSerializer


class UserSerializer(ModelSerializer):
    tweets = TweetSerializer(
        many=True,
    )

    class Meta:
        model = User
        fields = "id", "username", "tweets"
