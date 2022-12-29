import asyncio
import aioredis
import django
import websockets
import os
import json


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyrisk.settings')

django.setup()

CONNECTIONS = []

async def handler(websocket):
    CONNECTIONS.append(websocket)
    try:
        while True:
            message = await websocket.recv()
            print(message)
            websockets.broadcast(set(CONNECTIONS), message)
            print(len(CONNECTIONS))
    except Exception as e:
        print("connection close...........", str(e))
        CONNECTIONS.remove(websocket)

async def process_events():
    redis = aioredis.from_url("redis://127.0.0.1:6379/1")
    pubsub = redis.pubsub()
    await pubsub.subscribe("events")
    async for message in pubsub.listen():
        payload = message["data"].decode()
        websockets.broadcast(set(CONNECTIONS), payload)

async def main():
    async with websockets.serve(handler, "localhost", 8888):
        await process_events()
        # await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())

