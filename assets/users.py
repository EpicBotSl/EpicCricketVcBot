from config import Config
from pyrogram import Client
from pytgcalls import PyTgCalls
from helpers.log import LOGGER

USER = Client(
    Config.SESSION,
    Config.API_ID,
    Config.API_HASH,
    plugins=dict(root="assets")
    )
group_call = PyTgCalls(USER, cache_duration=180)
