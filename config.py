## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2", ""))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "2292721"))
API_HASH = getenv("API_HASH", "1e6685fae69a78d7fdbf02867c21d453")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://noobyash:noobyash@cluster0.0mptw.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Abhishek")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TASTRON")
ALIVE_NAME = getenv("ALIVE_NAME", "Abhishek")
BOT_USERNAME = getenv("BOT_USERNAME", "ABHI_DEAD_MUSIC_BOT")
OWNER_ID = getenv("OWNER_ID", "5286943475")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DEADABHIMUSIC_BOT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ABHI_WORLD_YAARON")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Some_Vibes")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/33dea3287e43d91996345.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/TASTRON")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
