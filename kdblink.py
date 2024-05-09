import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load

async def start():
    blink = Blink()
    auth = Auth(await json_load(r"C:\Code\kdblink\creditials.json"))
    await blink.save("C:\Code\kdblink\creditials.json")
    blink.auth = auth
    await blink.start()
    for name, camera in blink.cameras.items():
        print(name)                   # Name of the camera
        print(camera.attributes)      # Print available attributes of camera
    return blink



blink = asyncio.run(start())