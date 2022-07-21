import os
import asyncio
from bot import bot
from config import Config
from pyrogram import idle
from helpers.log import LOGGER
from helpers.utils import start_stream
from assets.user import group_call, USER
from pyrogram.errors import UserAlreadyParticipant


if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
else:
    for f in os.listdir("./downloads"):
        os.remove(f"./downloads/{f}")

async def main():
    await bot.start()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
