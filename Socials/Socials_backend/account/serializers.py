from .models import User
from rest_framework import serializers


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','name','email', 'get_avatar',)