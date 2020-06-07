import pytest
from channels.testing import WebsocketCommunicator

from channels_pro.routing import application


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_consumer_echo(fake, user):
    room = fake.word()
    message = fake.text()

    communicator = WebsocketCommunicator(application, f"ws/chat/{room}/")
    communicator.scope["user"] = user
    connected, subprotocol = await communicator.connect()

    assert connected

    await communicator.send_json_to({"message": message})

    response = await communicator.receive_json_from()

    assert response == {"message": message, "user": user.username}

    await communicator.disconnect()


@pytest.mark.asyncio
async def test_many_consumers_receive_message_from_one(fake, user):
    room = fake.word()
    message = fake.text()

    consumer_one_com = WebsocketCommunicator(application, f"ws/chat/{room}/")
    consumer_two_com = WebsocketCommunicator(application, f"ws/chat/{room}/")
    consumer_three_com = WebsocketCommunicator(application, f"ws/chat/{room}/")
    consumer_four_com = WebsocketCommunicator(application, f"ws/chat/{room}/")

    consumers = [
        consumer_one_com,
        consumer_two_com,
        consumer_three_com,
        consumer_four_com,
    ]

    for consumer in consumers:
        consumer.scope["user"] = user

        await consumer.connect()

    await consumer_one_com.send_json_to({"message": message})

    for consumer in consumers:
        response = await consumer.receive_json_from()

        assert response == {"message": message, "user": user.username}

        await consumer.disconnect()


@pytest.mark.asyncio
async def test_two_rooms_at_the_same_time(fake, user):
    room_one = fake.word()
    room_two = fake.word()

    message_one = fake.text()
    message_two = fake.text()

    connection_one = WebsocketCommunicator(application, f"ws/chat/{room_one}/")
    connection_two = WebsocketCommunicator(application, f"ws/chat/{room_two}/")

    connection_one.scope["user"] = user
    connection_two.scope["user"] = user

    await connection_one.connect()
    await connection_two.connect()

    await connection_one.send_json_to({"message": message_one})
    await connection_two.send_json_to({"message": message_two})

    response_one = await connection_one.receive_json_from()
    response_two = await connection_two.receive_json_from()

    assert response_one == {"message": message_one, "user": user.username}
    assert response_two == {"message": message_two, "user": user.username}

    assert response_one != {"message": message_two, "user": user.username}
    assert response_two != {"message": message_one, "user": user.username}


@pytest.mark.asyncio
async def test_typo_in_json_message(fake, user):
    room = fake.word()
    message = fake.sentence()

    communicator = WebsocketCommunicator(application, f"ws/chat/{room}/")

    communicator.scope["user"] = user

    connection = await communicator.connect()

    assert connection

    # Creating typo
    await communicator.send_json_to({'mesage': message})

    response = await communicator.receive_json_from()

    assert response != {'message': message, "user": user.username}
    assert response == {'message': 'Typo in message !!!', "user": user.username}
