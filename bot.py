import os
from config import Config
from config import *
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

bot = Client(
    "Epic Developers",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="module")
)

print(f"""@{uname} is Accepted
╔════╗────────╔═══╗
║╔╗╔╗║────────║╔══╝
╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
──────────────────║║
──────────────────╚╝
Join For update @EpicBotsSl""")

idle()
bot.start()

