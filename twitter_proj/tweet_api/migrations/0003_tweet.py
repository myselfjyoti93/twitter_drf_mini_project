# Generated by Django 3.1.7 on 2021-04-13 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_api', '0002_auto_20210414_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_hashtag', models.CharField(blank=True, max_length=255, null=True)),
                ('tweet_content', models.CharField(blank=True, max_length=255, null=True)),
                ('tweeted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('tweeted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tweet_api.user')),
            ],
            options={
                'db_table': 'tweets',
                'managed': True,
            },
        ),
    ]