from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("Hi, I am Forward Tag Removing Bot.\n\n"
                 "Just Forward me messages or\n"
                 "Files and I will Anonymize the\n"
                 "sender and Remove Forward Tag.\n\n"
                 "**Note:** __We Don't Promote Circulation of\n__"
                 "__Copyright Contents. This Bot is\n__"
                 "__Created for Educational Purpose\n__"
                 "__Only !!\n__")


if Credentials.START_MESSAGE is not None:
  START_TEXT = Credentials.START_MESSAGE
else:
  START_TEXT = DEFAULT_START
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,
                                message=START_TEXT,
                                buttons=[[Button.url("Bot's Updates Channel","http://t.me/Discovery_Updates")],
                                         [Button.url("Support & Discussion Group","http://t.me/linux_repo")]])                                                                 
    if event.message.media:
      await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass
    

with client:
  client.run_until_disconnected() 
