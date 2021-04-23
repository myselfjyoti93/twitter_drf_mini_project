from django.db import models


# Create your models here.

class TweetWebhook(models.Model):
    webhook_content = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    active_status = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'tweet_webhook'


class HashtagWebhook(models.Model):
    webhook_content = models.TextField(blank=True, null=True)
    hashtag = models.CharField(max_length=255, blank=True, null=True)
    active_status = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'hashtag_webhook'
