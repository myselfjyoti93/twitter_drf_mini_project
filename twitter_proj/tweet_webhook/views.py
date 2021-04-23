from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TweetWebhookSerializers, HashtagWebhookSerializers


# Create your views here.


class TopTenApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = TweetWebhookSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.create_tweet_webhook(request.data)
            return Response([response_data['data']], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

    def get(self, request, *args, **kwargs):
        serializer = TweetWebhookSerializers(data=request.query_params.dict())
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.get_tweet_webhook(request.query_params.dict())
            return Response(response_data['data'], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


class TopTenHastagApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = HashtagWebhookSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.create_hashtag_webhook(request.data)
            return Response([response_data['data']], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

    def get(self, request, *args, **kwargs):
        serializer = HashtagWebhookSerializers(data=request.query_params.dict())
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.get_hashtag_webhook(request.query_params.dict())
            return Response(response_data['data'], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
