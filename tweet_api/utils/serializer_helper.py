from ..models import User

import logging

from django.core.validators import URLValidator, EmailValidator
from django.core.exceptions import ValidationError

Logger = logging.getLogger('__name__')

class SerializerHelper:

    @staticmethod
    def is_valid_for_create(validated_data):
        username = validated_data['username']
        email_id = validated_data['email_id']
        user_obj = None
        return_val = False
        try:
            object_for_username_checking = User.objects.get(username=username)
            object_for_email_checking = User.objects.get(email_id=email_id)
            user_obj = User.objects.get(username=username, email_id=email_id)
        except Exception as ex:
            Logger.info("ex")
        if user_obj is None:
            return_val = True
        elif user_obj is not None and user_obj.active_status==0:
            return_val = True

        return return_val, user_obj

    @staticmethod
    def is_valid_username_and_email(validated_data):
        username = validated_data['username']
        email_id = validated_data['email_id']
        error_message = None
        return_val = True
        try:
            object_for_username_checking = None
            object_for_email_checking = None
            try:
                object_for_username_checking = User.objects.get(username=username)
            except Exception as ex:
                pass
            try:
                object_for_email_checking = User.objects.get(email_id=email_id)
            except Exception as ex:
                pass
            if object_for_username_checking is not None and object_for_username_checking.email_id != email_id:
                return_val = False
                error_message = f"username {username} is already in use"
            elif object_for_email_checking is not None and object_for_email_checking.username != username:
                return_val = False
                error_message = f"email_id {email_id} is already in use"
        except Exception as ex:
            Logger.info("ex")

        return return_val, error_message

    @staticmethod
    def get_fields_list():
        return [f.name for f in User._meta.fields]

    @staticmethod
    def is_valid_string(string_val):
        Logger.info(f"is_valid_string : Input : {string_val}")
        result = True
        if not isinstance(string_val, str):
            result = False
        elif string_val is None:
            result = False
        elif len(string_val) == 0:
            result = False
        elif string_val.isspace():
            result = False
        Logger.info(f"is_valid_string : Input : {result}")
        return result

    @staticmethod
    def validate_username(validated_data, return_val, error_message):
        if 'username' not in validated_data.keys():
            return_val = False
            error_message = 'username not in param'
        elif SerializerHelper.is_valid_string(validated_data['username']) is False:
            return_val = False
            error_message = 'Invalid value for username'
        return return_val, error_message

    @staticmethod
    def validate_email_id(validated_data, return_val, error_message):
        if 'email_id' not in validated_data.keys():
            return_val = False
            error_message = 'email_id not in param'
        elif SerializerHelper.is_valid_string(validated_data['email_id']) is False:
            return_val = False
            error_message = 'Invalid value for email_id'
        else:
            try:
                validate = EmailValidator()
                validate(validated_data['email_id'])
            except ValidationError as ex:
                return_val = False
                error_message = 'Invalid value for email_id'
        return return_val, error_message

    @staticmethod
    def validate_age(validated_data, return_val, error_message):
        if 'age' in validated_data.keys():
            if SerializerHelper.is_valid_string(validated_data['age']) is False:
                return_val = False
                error_message = 'Invalid value for age'
            if int(validated_data['age']) < 18:
                return_val = False
                error_message = 'User under age'
        return return_val, error_message

    @staticmethod
    def validate_address(validated_data, return_val, error_message):
        if 'address' in validated_data.keys():
            if SerializerHelper.is_valid_string(validated_data['address']) is False:
                return_val = False
                error_message = 'Invalid value for address'
        return return_val, error_message

    @staticmethod
    def validate_details(validated_data, return_val, error_message):
        if 'details' in validated_data.keys():
            if SerializerHelper.is_valid_string(validated_data['details']) is False:
                return_val = False
                error_message = 'Invalid value for details'
        return return_val, error_message

    @staticmethod
    def validate_other_param(validated_data, return_val, error_message):
        for param in validated_data.keys():
            if param != 'username' and param != 'email_id' and param != 'age' and param != 'address' and param != 'details':
                return_val = False
                error_message = 'Invalid param given'
        return return_val, error_message

    @staticmethod
    def is_valid_param_for_create(validated_data):
        return_val = True
        error_message = ''
        return_val, error_message = SerializerHelper.validate_other_param(validated_data, return_val, error_message)
        return_val, error_message = SerializerHelper.validate_details(validated_data, return_val, error_message)
        return_val, error_message = SerializerHelper.validate_address(validated_data, return_val, error_message)
        return_val, error_message = SerializerHelper.validate_age(validated_data, return_val, error_message)
        return_val, error_message = SerializerHelper.validate_email_id(validated_data, return_val, error_message)
        return_val, error_message = SerializerHelper.validate_username(validated_data, return_val, error_message)
        return return_val, error_message

    @staticmethod
    def validate_hashtag(validated_data, return_val, error_message):
        if 'tweet_hashtag' in validated_data.keys():
            if SerializerHelper.is_valid_string(validated_data['tweet_hashtag']) is False:
                return_val = False
                error_message = 'Invalid value for tweet_hashtag'
            elif validated_data['tweet_hashtag'].startswith('#') is False:
                return_val = False
                error_message = 'Invalid value for tweet_hashtag'
        return return_val, error_message

    @staticmethod
    def validate_content(validated_data, return_val, error_message):
        if 'tweet_content' not in validated_data.keys():
            return_val = False
            error_message = 'tweet_content not in param'
        elif SerializerHelper.is_valid_string(validated_data['tweet_content']) is False:
            return_val = False
            error_message = 'Invalid value for tweet_content'
        return return_val, error_message

    @staticmethod
    def validate_twitter_user(validated_data, return_val, error_message):
        if 'tweeted_by' not in validated_data.keys():
            return_val = False
            error_message = 'tweeted_by not in param'
        elif SerializerHelper.is_valid_string(validated_data['tweeted_by']) is False:
            return_val = False
            error_message = 'Invalid value for tweeted_by'
        return return_val, error_message

    @staticmethod
    def validate_other_param_for_tweet(validated_data, return_val, error_message):
        for param in validated_data:
            if param != 'username' and param != 'tweet_hashtag' and param != 'tweet_content':
                return_val = False
                error_message = 'Invalid param given'
        return return_val, error_message

    @staticmethod
    def is_valid_param_for_tweet(validated_data):
        return_val = True
        error_message = ''
        return_val, error_message = SerializerHelper.validate_content(validated_data, return_val, error_message)
        return_val, error_message = SerializerHelper.validate_hashtag(validated_data, return_val, error_message)
        return_val, error_message = SerializerHelper.validate_twitter_user(validated_data, return_val, error_message)
        return return_val, error_message

    @staticmethod
    def is_valid_param_for_get_tweet(validated_data):
        return_val = True
        error_message = ''
        return_val, error_message = SerializerHelper.validate_twitter_user(validated_data, return_val, error_message)
        if len(validated_data.keys()) > 1:
            return_val = False
            error_message = "Extra invalid param"
        return return_val, error_message

    @staticmethod
    def is_valid_param_for_get_hashtag(validated_data):
        return_val = True
        error_message = ''
        if 'tweet_hashtag' not in validated_data:
            return_val, error_message = False, 'tweet_hashtag not in param'
        return_val, error_message = SerializerHelper.validate_hashtag(validated_data, return_val, error_message)
        if len(validated_data.keys()) > 1:
            return_val = False
            error_message = "Extra invalid param"
        return return_val, error_message

    @staticmethod
    def check_valid_user(user):
        return_val = False
        user_obj = None
        try:
            user_obj = User.objects.get(username=user, active_status=1)
        except Exception as ex:
            pass
        if user_obj is not None:
            return_val = True
        return return_val