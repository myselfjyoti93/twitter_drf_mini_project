from django.contrib import admin
from django.urls import path
from .views import CreateUserApi, MakeTweetApi, GetTweetApi, GetHashtagApi

urlpatterns = [
    path('twitter/register', CreateUserApi.as_view(), name='Register'),
    path('twitter/tweet', MakeTweetApi.as_view(), name='Tweet'),
    path('twitter/get_tweets_of_user', GetTweetApi.as_view(), name='Get Tweets of user'),
    path('twitter/get_hastags', GetHashtagApi.as_view(), name='Get hastag'),
]