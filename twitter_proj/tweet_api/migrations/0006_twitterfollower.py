# Generated by Django 3.1.7 on 2021-04-13 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_api', '0005_auto_20210414_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'twitter_follwers',
                'managed': True,
            },
        ),
    ]
