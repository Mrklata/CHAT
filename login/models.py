from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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
