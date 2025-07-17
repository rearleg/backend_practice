from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer



@api_view()
def users(request):
    all_users = User.objects.all()
    serializer = UserSerializer(
        all_users,
        many=True,
    )
    return Response(serializer.data)


@api_view()
def user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    serializer = UserSerializer(user)
    return Response(serializer.data)
    