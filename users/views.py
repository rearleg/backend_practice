from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer


class UsersView(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)


class UserView(APIView):
    def get_objects(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        user = self.get_objects(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
