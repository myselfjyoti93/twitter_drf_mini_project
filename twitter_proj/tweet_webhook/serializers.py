from rest_framework import serializers, status

from .models import TweetWebhook, HashtagWebhook


class TweetWebhookSerializers(serializers.Serializer):
    class Meta:
        model = TweetWebhook
        fields = "__all__"

    def get_tweet_webhook(self, validated_data):
        response_data = dict(
            data=dict(
                data=[],
                message='',
                error='',
            ),
            status=status.HTTP_200_OK
        )
        try:
            tweet_webhook_obj = TweetWebhook.objects.filter(user=validated_data['user'])
            if len(tweet_webhook_obj) == 0:
                response_data['data']['data'] = []
                response_data['status'] = status.HTTP_204_NO_CONTENT
            else:
                tweet_webhook_obj = TweetWebhook.objects.get(user=validated_data['user'])
                response_data['data']['data'] = tweet_webhook_obj.webhook_content
        except Exception as ex:
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_data['error'] = ex
        return response_data

    def create_tweet_webhook(self, validated_data):
        response_data = dict(
            data=dict(
                data=[],
                message='',
                error='',
            ),
            status=status.HTTP_201_CREATED
        )
        try:
            tweet_webhook_obj = TweetWebhook.objects.filter(user=validated_data['user'])
            if len(tweet_webhook_obj) == 0:
                tweet_webhook_obj = TweetWebhook.objects.create(**validated_data)
            else:
                tweet_webhook_obj = TweetWebhook.objects.get(user=validated_data['user'])
                tweet_webhook_obj.webhook_content = validated_data['webhook_content']
            tweet_webhook_obj.active_status = 1
            tweet_webhook_obj.save()
        except Exception as ex:
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_data['error'] = ex
        response_data['status'] = status.HTTP_201_CREATED
        return response_data


class HashtagWebhookSerializers(serializers.Serializer):
    class Meta:
        model = HashtagWebhook
        fields = "__all__"

    def get_hashtag_webhook(self, validated_data):
        response_data = dict(
            data=dict(
                data=[],
                message='',
                error='',
            ),
            status=status.HTTP_200_OK
        )
        try:
            hashtag_webhook_obj = HashtagWebhook.objects.filter(hashtag=validated_data['hashtag'])
            if len(hashtag_webhook_obj) == 0:
                response_data['data']['data'] = []
                response_data['status'] = status.HTTP_204_NO_CONTENT
            else:
                hashtag_webhook_obj = HashtagWebhook.objects.get(hashtag=validated_data['hashtag'])
                response_data['data']['data'] = hashtag_webhook_obj.webhook_content
        except Exception as ex:
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_data['error'] = ex
        return response_data

    def create_hashtag_webhook(self, validated_data):
        response_data = dict(
            data=dict(
                data=[],
                message='',
                error='',
            ),
            status=status.HTTP_201_CREATED
        )
        try:
            hashtag_webhook_obj = HashtagWebhook.objects.filter(hashtag=validated_data['hashtag'])
            if len(hashtag_webhook_obj) == 0:
                hashtag_webhook_obj = HashtagWebhook.objects.create(**validated_data)
            else:
                hashtag_webhook_obj = HashtagWebhook.objects.get(hashtag=validated_data['hashtag'])
                hashtag_webhook_obj.webhook_content = validated_data['webhook_content']
            hashtag_webhook_obj.active_status = 1
            hashtag_webhook_obj.save()
        except Exception as ex:
            response_data['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            response_data['error'] = ex
        response_data['status'] = status.HTTP_201_CREATED
        return response_data
