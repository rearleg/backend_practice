from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer


# Create your views here.
@api_view()
def tweets(request):
    tweet = Tweet.objects.all()
    serializer = TweetSerializer(
        tweet,
        many=True,
    )
    return Response(serializer.data)
