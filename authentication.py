import twitter
from django.core.exceptions import PermissionDenied
from Challenge_task import settings


def verify_credentials():
    try:
        twitter_api = twitter.Api(
            consumer_key=settings.CONSUMER_KEY,
            consumer_secret=settings.CONSUMER_SECRET,
            access_token_key=settings.ACESS_TOKEN_KEY,
            access_token_secret=settings.ACESS_TOKEN_SECRET
        )
        twitter_api.VerifyCredentials()

    except Exception:
        raise PermissionDenied

    return twitter_api
