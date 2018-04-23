from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import exceptions

from .serializer import HomeTimelineSerializer, PostUpdateSerializer
from authentication import verify_credentials

from .models import RequestLog, Tweet


class SimpleView(APIView):
    """

    View for posting tweet and getting home timeline.

    **Example requests**:

        GET /twitter/
        POST /twitter/
        DATA - {tweet}

    """

    def finalize_response(self, request, response, *args, **kwargs):
        path = request.get_full_path()
        log = request.get_host() + path + ' ' + str(response.status_code)
        RequestLog.objects.create(request_log=log)
        return super(SimpleView, self).finalize_response(request, response, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        api = verify_credentials()
        Tweet.objects.all().delete()

        try:
            timeline = api.GetHomeTimeline()

            for tweet in timeline:
                Tweet.objects.create(text=tweet.text)

        except exceptions.APIException:
            raise exceptions.ParseError

        queryset = Tweet.objects.all()
        serializer = HomeTimelineSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
         api = verify_credentials()
         serializer = PostUpdateSerializer(data=request.data)

         if serializer.is_valid():
             try:
                 api.PostUpdate(serializer.data.get('tweet'))

             except exceptions.APIException:
                 raise exceptions.ParseError
             return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







