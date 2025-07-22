from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer, UserDetailSerializer, UserTweetsSerializer


class UsersList(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    def get(self, request, pk):
        get_user = User.objects.get(pk=pk)
        serializer = UserDetailSerializer(get_user)
        return Response(serializer.data)


class UserTweets(APIView):
    def get_objects(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        user = self.get_objects(pk)
        serializer = UserTweetsSerializer(user)
        return Response(serializer.data)
