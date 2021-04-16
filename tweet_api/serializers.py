from rest_framework import serializers, status
from .models import User, Tweet
from .utils.serializer_helper import SerializerHelper

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