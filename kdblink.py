import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth

async def start():
    blink = Blink(session=ClientSession())
    # Can set no_prompt when initializing auth handler
    auth = Auth({"username": <username>, "password": <your password>}, no_prompt=True)
    blink.auth = auth
    await blink.start()
    return blink

blink = asyncio.run(start())