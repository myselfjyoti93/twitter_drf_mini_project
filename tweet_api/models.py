from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    active_status = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'twitter_user'

class Tweet(models.Model):
    tweet_hashtag = models.CharField(max_length=255, blank=True, null=True)
    tweet_content = models.CharField(max_length=255, blank=True, null=True)
    tweeted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tweeted_by = models.ForeignKey(User, on_delete=models.PROTECT, db_column='tweeted_by')
    active_status = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'tweets'

class TwitterFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=-1)
    follower = models.ForeignKey(User, related_name='follower_user', on_delete=models.PROTECT, default=-1)
    active_status = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'twitter_follwers'



