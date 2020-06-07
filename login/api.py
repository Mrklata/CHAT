from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
# from rest_framework.decorators import action

from login.serializers import UserSerializer, PostsSerializer, ProfileSerializer
# from login.serializers import FriendRequestSerializer, FriendResponseSerializer
from login.models import Post, Profile
# from login.models import FriendRequest


class CreateUserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


# class FriendRequestView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     model = FriendRequest
#     serializer_class = FriendRequestSerializer
#
#     def perform_create(self, serializer):
#         return serializer.save(from_user=self.request.user, timestamp='pending')

    # @action(detail=True, methods=["post"])
    # def response(request, *args, **kwargs):
    #     ser = FriendResponseSerializer(data=request.data)
    #     ser.is_valid(raise_exception=True)
    #     data = ser.validated_data


class CreateProfileView(viewsets.GenericViewSet, mixins.ListModelMixin):
    model = Profile
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class CreatePostsView(viewsets.ModelViewSet):
    model = Post
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        return Post.objects.filter(user=user)
