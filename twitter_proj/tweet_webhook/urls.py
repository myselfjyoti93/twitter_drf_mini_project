from django.urls import path

from .views import TopTenApi, TopTenHastagApi

urlpatterns = [
    path('twitter/top_ten_tweets', TopTenApi.as_view()),
    path('twitter/trending_hashtags', TopTenHastagApi.as_view()),
]
