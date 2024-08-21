import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

response = requests.get('https://api.ipify.org?format=json')
ip = response.json()['ip']
print(f'Public IP Address: {ip}')


# Load the .env file
load_dotenv()

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Owner User name and Owner Id
OWNER = os.environ.get("OWNER", "")  
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

# Your Mongo Url 
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")

# Telegram Channel Id's
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))


SECONDS = int(os.getenv("SECONDS", "600"))  # Auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "1"))


# Start message
START_MSG = os.environ.get(
    "START_MESSAGE", "Yo {first} {last}\n\nI am File Store i provide you coolest file on internet")

try:
    ADMINS = [6450266465]
    for x in (os.environ.get("ADMINS", "1768198143 6450266465 7065803173").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE", "<b><center> 🌸 𝙆𝙤𝙣𝙣𝙞𝙘𝙝𝙞𝙬𝙖, 𝙛𝙚𝙡𝙡𝙤𝙬 𝙤𝙩𝙖𝙠𝙪! 🌸 </center>\n\n 𝙄𝙛 𝙮𝙤𝙪’𝙧𝙚 𝙖 𝙩𝙧𝙪𝙚 𝙨𝙚𝙣𝙥𝙖𝙞, 𝙟𝙤𝙞𝙣 𝙢𝙮 𝙘𝙝𝙖𝙣𝙣𝙚𝙡𝙨 𝙖𝙣𝙙 𝙡𝙚𝙩’𝙨 𝙬𝙚𝙖𝙫𝙚 𝙤𝙪𝙧 𝙖𝙣𝙞𝙢𝙚 𝙢𝙖𝙜𝙞𝙘 𝙩𝙤𝙜𝙚𝙩𝙝𝙚𝙧! 🎉 𝙇𝙚𝙩’𝙨 𝙨𝙥𝙧𝙞𝙣𝙠𝙡𝙚 𝙖 𝙡𝙞𝙩𝙩𝙡𝙚 “𝙠𝙖𝙬𝙖𝙞𝙞” 𝙞𝙣𝙩𝙤 𝙤𝙪𝙧 𝙘𝙤𝙣𝙫𝙚𝙧𝙨𝙖𝙩𝙞𝙤𝙣𝙨, 𝙗𝙚𝙘𝙖𝙪𝙨𝙚 𝙡𝙞𝙛𝙚 𝙞𝙨 𝙗𝙚𝙩𝙩𝙚𝙧 𝙬𝙞𝙩𝙝 𝙖 𝙩𝙤𝙪𝙘𝙝 𝙤𝙛 𝙅𝙖𝙥𝙖𝙣𝙚𝙨𝙚 𝙛𝙡𝙖𝙞𝙧. 🌟🇯🇵</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get(
    'PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get(
    "DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ʙᴀᴋᴀᴀ! ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴍᴇ ᴍᴇꜱꜱᴀɢᴇ"

ADMINS.append(OWNER_ID)
ADMINS.append(6450266465)



# Don't Change Any Think Here 
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


try:
    # Connect to MongoDB
    client = pymongo.MongoClient(DB_URL)
    db = client[DB_NAME]  # Specify the database to use
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

client = MongoClient(DB_URL, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
