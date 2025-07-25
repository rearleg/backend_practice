from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ParseError, ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializers import (
    UserSerializer,
    UserDetailSerializer,
    UserTweetsSerializer,
    PrivateUserSerializer,
)


class UsersList(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_users = User.objects.all()
        serializer = PrivateUserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 패스워드
        password = request.data.get("password")
        if not password:
            raise ParseError
        if len(password) < 8:
            raise ValidationError("비밀번호는 8글자 이상이어야 합니다.")

        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserDetail(APIView):

    permission_classes = [IsAuthenticated]

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


class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class LogIn(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response(status=HTTP_200_OK)
        else:
            return Response({"error": "Wrong Password!"})


class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=HTTP_200_OK)
