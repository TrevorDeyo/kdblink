import os
import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load



async def start():
    blink = Blink()
    
    # Get cwd to find the creds file after moving to linux server so I dont have to edit the code later
    creds = os.getcwd() + r"\credentials.json"
    
    # loads creds
    if os.path.exists(creds):
        auth = Auth(await json_load(creds))
    else:
    # if creds doesn't exist make it
        await blink.save(creds)
    
    blink.auth = auth
    await blink.start()
    return blink


blink = asyncio.run(start())

# grab camera names
for name, camera in blink.cameras.items():
    print(name)                   # Name of the camera
    print(camera.attributes)      # Print available attributes of camera