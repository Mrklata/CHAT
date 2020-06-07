import pytest
from django.urls import reverse
from model_bakery import baker

from login.models import Post


@pytest.mark.django_db
def test_get_queryset(fake, user, django_user_model, user_client):
    baker.make(Post, user=user, _quantity=10)

    wrong_post = Post.objects.create(
        user=baker.make(django_user_model, username=fake.name()),
        title=fake.sentence(),
        text=fake.text(),
    )

    response = user_client.get(reverse("post-list"))

    assert response.status_code == 200
    assert len(response.data) == 10
    assert not any(entry["id"] == wrong_post.id for entry in response.data)

# TODO
# @pytest.mark.django_db
# def test_perform_create(user_client, fake):
#     post_data = {"title": fake.sentence(), "text": fake.text()}
#
#     response = user_client.post(reverse("post-list"), data=post_data)
#
#     assert Post.objects.all().count() == 1
