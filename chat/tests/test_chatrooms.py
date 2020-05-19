import pytest
from channels.testing import WebsocketCommunicator

from channels_pro.routing import application


@pytest.mark.asyncio
async def test_consumer(fake):
    room = fake.word()
    wrong_room = fake.word()

    message = fake.text()

    communicator = WebsocketCommunicator(application, f"ws/chat/{room}/")
    wrong_communicator = WebsocketCommunicator(application, f"ws/chat/{wrong_room}/")

    wrong_connected = await wrong_communicator.connect()
    connected = await communicator.connect()

    assert connected
    assert wrong_connected

    await communicator.send_json_to({"message": message})

    response = await communicator.receive_json_from()

    try:
        wrong_response = await wrong_communicator.receive_json_from()
    except:
        wrong_response = None

    assert response == {"message": message}
    assert not wrong_response

    await communicator.disconnect()
    await wrong_communicator.disconnect()


@pytest.mark.asyncio
async def test_consumers(fake):
    room = fake.word()
    message = fake.text()

    consumer_one_com = WebsocketCommunicator(application, f"ws/chat/{room}/")
    consumer_two_com = WebsocketCommunicator(application, f"ws/chat/{room}/")
    consumer_three_com = WebsocketCommunicator(application, f"ws/chat/{room}/")
    consumer_four_com = WebsocketCommunicator(application, f"ws/chat/{room}/")

    consumers = [consumer_one_com, consumer_two_com, consumer_three_com, consumer_four_com]

    for consumer in consumers:
        await consumer.connect()

    await consumer_one_com.send_json_to({"message": message})

    for consumer in consumers:
        response = await consumer.receive_json_from()

        assert response == {'message': message}

        await consumer.disconnect()
