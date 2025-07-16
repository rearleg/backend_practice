from django.shortcuts import render
from .models import Tweet


# Create your views here.
def see_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "see_tweets.html",
        {
            "tweets": tweets,
            "title": "See All Tweets",
        },
    )
