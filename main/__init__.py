#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "12842782"
API_HASH = "b9af9690e4e36df1f8d356e1a8e376a9"
BOT_TOKEN = "5961413879:AAFvwFP5-STmvAo2J34wZo19J8JmAmISB48"
SESSION = "BQBlUUJNRToWtoyTUQTJ3pg11pjh-AN0FSaa6-5DkfajnecLvqPvd3-fD8VAhdYtc0znW1wnwsIoi58otyK-VYxUsKa_rfLUICdoGnTlbawyeQmyYpy43hBZypuBJR3O5b5ZpabkrIdIOgZkv_GDnaTFeAH6q-7IM7yFJXWf2RS8KQdupbHFVyCPExfpAiSg7Ap3-Sw3HlcHGWlEjRgY0ujOHC64ocbiiaX0iDtQsVoBt-o-n9DFUjQvObjLHch4neICFtoUI_rS6_cXclUJAOBPjHOUcy-fMl8e8YaNpqYBPiZt4s8qa1Kgw5MMzipfRXsLeWhrsZFLxQZA2rymBghEAAAAAVHqXYkA"
FORCESUB = "restrictedsaverwarnisx"
AUTH = "5669281161"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
