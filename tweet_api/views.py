from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializers, TweetSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

class CreateUserApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.create_user(request.data)
            return Response(response_data['data'], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

class MakeTweetApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = TweetSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.make_tweet(request.data)
            return Response(response_data['data'], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

class GetTweetApi(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        data = request.query_params.dict()
        serializer = TweetSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.get_tweet(data)
            return Response(response_data['data'], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

class GetHashtagApi(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        data = request.query_params.dict()
        serializer = TweetSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.get_hastag_details(data)
            return Response(response_data['data'], status=response_data['status'], content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")