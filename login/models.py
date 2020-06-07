from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('Profile', blank=True)

    def __str__(self):
        return self.user.username

    # TODO
    def get_absolute_url(self):
        pass


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", null=True
    )
    title = models.CharField(max_length=125)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"


# class FriendRequest(models.Model):
#     STATUSES = (
#         ('pending',  'pending'),
#         ('declined', 'declined'),
#         ('accepted', 'accepted')
#     )
#
#     from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
#     to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
#     timestamp = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=10, choices=STATUSES)
#
#     def __str__(self):
#         return f'From {self.from_user.username} to {self.to_user.username}'
#
#     class Meta:
#         verbose_name = 'request'
#         verbose_name_plural = 'requests'
#         unique_together = ['from_user', 'to_user']
