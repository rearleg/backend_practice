from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from .models import Tweet
from .serializers import TweetSerializer


class Tweets(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(
            all_tweets,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            created_tweet = serializer.save(user=request.user)
            return Response(TweetSerializer(created_tweet).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class TweetDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_objects(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_objects(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_objects(pk)
        if tweet.user != request.user:
            raise PermissionDenied
        serializer = TweetSerializer(
            tweet,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(TweetSerializer(updated_tweet).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tweet = self.get_objects(pk)
        if tweet.user != request.user:
            raise PermissionDenied
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
