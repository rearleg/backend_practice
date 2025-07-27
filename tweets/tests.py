from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestTweets(APITestCase):

    PAYLOAD = "와 이번 테스트 미쳤네"
    USERNAME = "test"
    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(username=self.USERNAME)
        user.set_password("123")
        user.save()
        self.user = user

        models.Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_all_tweets(self):

        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(response.status_code, 200),
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            data[0]["payload"],
            self.PAYLOAD,
        )
        self.assertEqual(
            data[0]["user"],
            self.USERNAME,
        )

    def test_create_tweet(self):

        new_payload = "크크크크 진짜 웃기당."

        response = self.client.post("/api/v1/tweets/")
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)

        response = self.client.post(
            self.URL,
            data={
                "payload": new_payload,
            },
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["payload"], new_payload)
        self.assertEqual(data["user"], self.USERNAME)

        response = self.client.post("/api/v1/tweets/", data={"payload": "a" * 1000})
        self.assertEqual(response.status_code, 400)


class TestTweet(APITestCase):

    PAYLOAD = "와 이번 테스트 미쳤네"
    USERNAME = "test"
    URL = "/api/v1/tweets/1/"

    def setUp(self):
        user = User.objects.create(username=self.USERNAME)
        user.set_password("123")
        user.save()
        self.user = user

        models.Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_get_tweet(self):
        response = self.client.get(self.URL)
        self.assertEqual(
            response.status_code,
            403,
        )

        self.client.force_login(self.user)

        response = self.client.get("/api/v1/tweets/2/")
        self.assertEqual(
            response.status_code,
            404,
        )

        response = self.client.get(
            self.URL,
        )
        self.assertEqual(
            response.status_code,
            200,
        )
        data = response.json()
        self.assertEqual(
            data["payload"],
            self.PAYLOAD,
        )
        self.assertEqual(
            data["user"],
            self.USERNAME,
        )

    def test_put_tweet(self):
        new_payload = "곰 세마리가 한 집에 있어"

        self.client.force_login(self.user)

        response = self.client.put(
            self.URL,
            data={"payload": new_payload},
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["payload"], new_payload)

        response = self.client.put(self.URL, data={"payload":"a"*1000})
        self.assertEqual(response.status_code, 400)

    def test_delete_tweet(self):

        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)

        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 204)