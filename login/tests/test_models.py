import pytest

from login.models import Post


@pytest.mark.django_db
def test_create_object(create_post):
    create_post

    post = Post.objects.all()

    assert post.count() == 1


@pytest.mark.django_db
def test_get_url(create_post, user_client):
    post = create_post

    url = post.get_absolute_url()
    response = user_client.get(url)

    assert response.data["id"] == post.id


@pytest.mark.django_db
def test_str(create_post):
    post = create_post
    assert type(post.title) == str
