from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    

# class TokenObtainSerializer(serializers.Serializer):
#     username_field = User.USERNAME_FIELD

#     default_error_messages = {
#         'no_active_account': ('No active account found with the given credentials')
#     }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields[self.username_field] = serializers.CharField()
#         self.fields['password'] = serializers.CharField()

#     def validate(self, attrs):
#         authenticate_kwargs = {
#             self.username_field: attrs[self.username_field],
#             'password': attrs['password'],
#         }
#         try:
#             authenticate_kwargs['request'] = self.context['request']
#         except KeyError:
#             pass

#         self.user = authenticate(**authenticate_kwargs)

#         if self.user is None or not self.user.is_active:
#             raise exceptions.AuthenticationFailed(
#                 self.error_messages['no_active_account'],
#                 'no_active_account',
#             )

#         return {}

#     @classmethod
#     def get_token(cls, user):
#         raise NotImplementedError('Must implement `get_token` method for `TokenObtainSerializer` subclasses')


# class TokenObtainPairSerializer(TokenObtainSerializer):
#     @classmethod
#     def get_token(cls, user):
#         return RefreshToken.for_user(user)

#     def validate(self, attrs):
#         data = super().validate(attrs)

#         refresh = self.get_token(self.user)

#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)

#         return data