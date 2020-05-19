from faker import Faker
import pytest
from model_bakery import baker

from login.models import Post


@pytest.fixture(scope="session")
def fake():
    return Faker()


@pytest.fixture
def user_data(fake):
    return {
        "username": fake.name(),
        "password": fake.password(),
    }


@pytest.fixture
def user(user_data, django_user_model):
    user = baker.make(django_user_model, **user_data)
    user.set_password(user_data["password"])
    user.save()
    return user


@pytest.fixture
def user_client(client, user_data):
    client.login(username=user_data["username"], password=user_data["password"])
    return client


@pytest.fixture
def create_post(user):
    return baker.make(
        Post,
        user=user
    )
