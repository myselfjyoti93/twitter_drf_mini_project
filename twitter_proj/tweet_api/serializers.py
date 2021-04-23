from rest_framework import serializers, status
from .models import User, Tweet
from .utils.serializer_helper import SerializerHelper
import requests
import json
from django.conf import settings

class UserSerializers(serializers.Serializer, SerializerHelper):
    class Meta:
        model = User
        fields = "__all__"

    def create_user(self, validated_data):
        validated_data = validated_data.dict()
        response_data = dict(
            data=dict(
                data=validated_data,
                message='',
                error='',
            ),
            status=status.HTTP_201_CREATED
        )
        try:
            return_val, error_message = UserSerializers.is_valid_param_for_create(validated_data)
            if return_val is False:
                response_data['data']['error'] = error_message
                response_data['status'] = status.HTTP_400_BAD_REQUEST
            else:
                is_valid, user_obj = SerializerHelper.is_valid_for_create(validated_data)
                return_val, error_message = SerializerHelper.is_valid_username_and_email(validated_data)
                if return_val is False:
                    response_data['data']['error'] = error_message
                    response_data['status'] = status.HTTP_400_BAD_REQUEST
                elif is_valid is True and user_obj is None:
                    user_obj = User.objects.create(**validated_data)
                    user_obj.active_status = 1
                    user_obj.save()
                    response_data['data']['message'] = "Created Successfully"
                elif is_valid is True and user_obj is not None:
                    user_obj.active_status = 1
                    for key in validated_data.keys():
                        setattr(user_obj, key, validated_data[key])
                    user_obj.save()
                    response_data['data']['message'] = "Created Successfully"
                else:
                    response_data['data']['error'] = "Create error, Record already exist"
                    response_data['status'] = status.HTTP_409_CONFLICT
        except Exception as ex:
            response_data['data']['error'] = ex
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response_data

class TweetSerializers(serializers.Serializer, SerializerHelper):
    class Meta:
        model = Tweet
        fields = "__all__"

    def make_tweet(self, validated_data):
        validated_data = validated_data.dict()
        response_data = dict(
            data=dict(
                data=validated_data,
                message='',
                error='',
            ),
            status=status.HTTP_201_CREATED
        )
        try:
            return_val, error_message = TweetSerializers.is_valid_param_for_tweet(validated_data)
            if return_val is False:
                response_data['data']['error'] = error_message
                response_data['status'] = status.HTTP_400_BAD_REQUEST
            elif TweetSerializers.check_valid_user(validated_data['tweeted_by']) is False:
                response_data['data']['error'] = f"{validated_data['tweeted_by']} not a valid user"
                response_data['status'] = status.HTTP_400_BAD_REQUEST
            else:
                tweeted_by = validated_data['tweeted_by']
                validated_data['tweeted_by'] = User.objects.get(username=validated_data['tweeted_by'])
                tweet_obj = Tweet.objects.create(**validated_data)
                tweet_obj.save()
                response_data['data']['message'] = "Tweeted Successfully"
                #Update Webhook
                total_tweets_by_user = Tweet.objects.filter(tweeted_by=validated_data['tweeted_by'])
                if total_tweets_by_user.count() > 10 and hasattr(settings, 'WEBHOOK_URL_FOR_TOP_TEN_TWEETS_BY_USER') is True:
                    last_ten_tweets_by_user = total_tweets_by_user.order_by('-tweeted_at').values('tweet_hashtag', 'tweet_content', 'tweeted_at')[: 10]
                    webhook_url = settings.WEBHOOK_URL_FOR_TOP_TEN_TWEETS_BY_USER
                    last_ten_tweets = ",".join([str(tweets_by_user) for tweets_by_user in last_ten_tweets_by_user])
                    last_ten_tweets_by_user = dict(
                        user=tweeted_by,
                        webhook_content=last_ten_tweets
                    )
                    send_webhook = requests.post(webhook_url, data=json.dumps(last_ten_tweets_by_user), headers={'Content-Type': 'application/json'})
                # Update Webhook
                total_tweets_with_hashtag = Tweet.objects.filter(tweet_hashtag=validated_data['tweet_hashtag'])
                if total_tweets_with_hashtag.count() > 10 and hasattr(settings, 'WEBHOOK_URL_FOR_TRENDING_TWEETS_WITH_HASHTAG') is True:
                    webhook_url = settings.WEBHOOK_URL_FOR_TRENDING_TWEETS_WITH_HASHTAG
                    las_ten_tweets_with_hashtag = total_tweets_with_hashtag.order_by('-tweeted_at').values('tweeted_by', 'tweet_content', 'tweeted_at')[: 10]
                    for tweets in las_ten_tweets_with_hashtag:
                        tweets['tweeted_by'] = User.objects.get(id=tweets['tweeted_by']).username
                    last_ten_tweets = ",".join([str(tweets_with_hashtag) for tweets_with_hashtag in las_ten_tweets_with_hashtag])
                    last_ten_tweets_with_hashtag = dict(
                        hashtag=validated_data['tweet_hashtag'],
                        webhook_content=last_ten_tweets
                    )
                    send_webhook = requests.post(webhook_url, data=json.dumps(last_ten_tweets_with_hashtag), headers={'Content-Type': 'application/json'})
                validated_data['tweeted_by'] = tweeted_by
        except Exception as ex:
            response_data['data']['error'] = ex
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response_data

    def get_tweet(self, validated_data):
        response_data = dict(
            data=dict(
                data=validated_data,
                message='',
                error='',
            ),
            status=status.HTTP_200_OK
        )
        try:
            return_val, error_message = TweetSerializers.is_valid_param_for_get_tweet(validated_data)
            if return_val is False:
                response_data['data']['error'] = error_message
                response_data['status'] = status.HTTP_400_BAD_REQUEST
            elif TweetSerializers.check_valid_user(validated_data['tweeted_by']) is False:
                response_data['data']['error'] = f"{validated_data['tweeted_by']} not a valid user"
                response_data['status'] = status.HTTP_400_BAD_REQUEST
            else:
                user = User.objects.get(username=validated_data['tweeted_by'])
                tweet_obj = Tweet.objects.filter(tweeted_by=user).order_by('-tweeted_at').values(
                'tweet_hashtag', 'tweet_content', 'tweeted_at')[:10][::-1]
                response_data['data']['data'] = tweet_obj
                response_data['data']['message'] = "Tweet retrieved Successfully"
        except Exception as ex:
            response_data['data']['error'] = ex
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response_data


    def get_hastag_details(self, validated_data):
        response_data = dict(
            data=dict(
                data=validated_data,
                message='',
                error='',
            ),
            status=status.HTTP_200_OK
        )
        try:
            return_val, error_message = TweetSerializers.is_valid_param_for_get_hashtag(validated_data)
            if return_val is False:
                response_data['data']['error'] = error_message
                response_data['status'] = status.HTTP_400_BAD_REQUEST
            else:
                tweet_hashtag = validated_data['tweet_hashtag']
                tweet_obj = Tweet.objects.filter(tweet_hashtag=tweet_hashtag).order_by('-tweeted_at').values(
                'tweet_content', 'tweeted_at', 'tweeted_by')[:100][::-1]
                for tweet in tweet_obj:
                    tweet['tweeted_by'] = User.objects.get(id=tweet['tweeted_by']).username
                response_data['data']['data'] = tweet_obj
                response_data['data']['message'] = f"Tweet with hashtag {tweet_hashtag} retrieved Successfully"
        except Exception as ex:
            response_data['data']['error'] = ex
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response_data