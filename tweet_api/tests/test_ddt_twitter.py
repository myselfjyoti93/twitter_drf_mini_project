from ddt import ddt, file_data
from django.test import Client
from django.test import TestCase
from datetime import datetime
from django.utils import timezone
import time


from ..models import User, Tweet


@ddt
class TestTwitter(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(username='user2', email_id='user2@gmail.com', active_status=0)
        User.objects.create(username='user3', email_id='user3@gmail.com', active_status=1)
        User.objects.create(username='user4', email_id='user4@gmail.com', active_status=1)
        Tweet.objects.create(tweet_hashtag="#ABC", tweet_content="ABC", tweeted_at=datetime.now(tz=timezone.utc), tweeted_by=User.objects.get(username='user4'))
        time.sleep(1)
        Tweet.objects.create(tweet_hashtag="#ABC", tweet_content="ABC", tweeted_at=datetime.now(tz=timezone.utc), tweeted_by=User.objects.get(username='user4'))
        time.sleep(1)
        Tweet.objects.create(tweet_hashtag="#ABC", tweet_content="ABC", tweeted_at=datetime.now(tz=timezone.utc), tweeted_by=User.objects.get(username='user4'))
        time.sleep(1)
        Tweet.objects.create(tweet_hashtag="#ABC", tweet_content="ABC", tweeted_at=datetime.now(tz=timezone.utc), tweeted_by=User.objects.get(username='user4'))
        time.sleep(1)
        Tweet.objects.create(tweet_hashtag="#ABC", tweet_content="ABC", tweeted_at=datetime.now(tz=timezone.utc), tweeted_by=User.objects.get(username='user4'))

    @file_data('../data/test_data_twitter.json')
    def test_twitter(self, url, method, input, expected_output):
        # Setup Part
        payload = input

        # Response Part
        if method == "GET":
            response = self.client.get(
                url, payload
            )
        elif method == "POST":
            response = self.client.post(
                url, payload
            )

        # Assert Part

        response_json = response.json()
        self.assertEqual(response.status_code, expected_output['status_code'])
        self.assertEqual(response_json['message'], expected_output['data']['message'])
        self.assertEqual(response_json['error'], expected_output['data']['error'])
        self.assertEqual(response_json['data'], expected_output['data']['data'])
