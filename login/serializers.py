from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator

from login.models import Post, Profile
# from login.models import FriendRequest
UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email", "first_name", "last_name")
        write_only_fields = ("password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        return user


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "user")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "friends")
        read_only_fields = ("id", "friends")


# class FriendRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FriendRequest
#         fields = "__all__"
#         read_only_fields = ("from_user", "timestamp", "status")
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=FriendRequest.objects.all(),
#                 fields=['from_user', 'to_user']
#             )
#         ]
#     # https://www.django-rest-framework.org/api-guide/validators/
#
#     def create(self, validated_data):
#         friend_request = FriendRequest.objects.create(
#             to_user=validated_data["to_user"]
#         )
#         return friend_request
#
# class FriendResponseSerializer(serializers.Serializer):
#     accept = serializers.BooleanField(required=True)
