from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import UserSerilaizer
from posts.models import Post
from posts.serializers import PostSerilaizer


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    users = User.objects.filter(name__icontains=query)
    users_serializer = UserSerilaizer(users, many=True)

    posts = Post.objects.filter(body__icontains=query)
    posts_serializer = PostSerilaizer(posts, many=True)

    return JsonResponse({
        'users': users_serializer.data,
        'posts': posts_serializer.data
    }, safe=False)