from rest_framework.serializers import ModelSerializer
from .models import User
from tweets.serializers import TweetSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "is_staff",
            "first_name",
            "last_name",
            "last_login",
        ]


class UserTweetsSerializer(ModelSerializer):

    tweets = TweetSerializer(
        many=True,
    )

    class Meta:
        model = User
        fields = "id", "username", "tweets"


class PrivateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )