# ZELDA-BOT
from time import sleep
from userbot import ALIVE_NAME, CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname()
# ============================================

