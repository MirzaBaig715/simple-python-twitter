from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
import pytest


class TwitterTestCase(APITestCase):
    """
    Test suite for the api views.

    """

    @pytest.mark.django_db
    def test_api_post_tweet(self):
        """
        Test the api has post tweet creation capability.

        Command:
        pytest twitterapp/tests

        """
        self.tweet_data = {
            'tweet': 'The most useful comments are those written with the goal '
                     'of learning from or helping out other readers—after reading '
                     'the whole article and all the earlier comments.'
        }

        self.post_response = self.client.post(reverse('twitter'), self.tweet_data)
        self.assertEqual(self.post_response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_api_get_timeline(self):
        """
        Test the api to get an home timeline.

        Command:
        pytest twitterapp/tests

        """

        response = self.client.get(reverse('twitter'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
