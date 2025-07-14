from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    payload = models.TextField(
        max_length=180,
    )
    user = models.ForeignKey(
        "users.user",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} : {self.payload}"


class Like(CommonModel):
    user = models.ForeignKey(
        "users.user",
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        "tweets.tweet",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return "like"
