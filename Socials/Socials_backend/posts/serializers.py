from .models import Post
from account.serializers import UserSerilaizer
from rest_framework import serializers


class PostSerilaizer(serializers.ModelSerializer):
    created_by=UserSerilaizer(read_only=True)
    class Meta:
        model=Post
        fields=('id','body','created_by','created_at_formatted',)