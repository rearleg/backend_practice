from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Tweet
from users.tserializers import TinyUserSerializer


class TweetSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Tweet
        fields = (
            "id",
            "user",
            "payload",
        )

    def get_user(self, tweet):
        return tweet.user.username