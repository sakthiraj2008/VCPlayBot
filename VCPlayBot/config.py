import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("8151794254:AAGR5hvAu9yM413eXWoBkI6CtIQMz7HzH5A")
BOT_NAME = getenv("Miss Clara Chan")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tn_Botz")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("11472991"))
API_HASH = getenv("c78c50d54baf2173e8b3f75c359c0c72")
BOT_USERNAME = getenv("miss_clara_chan_bot)
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Alexxa")
OWNER_NAME = getenv("OWNER_NAME", "Offx SNE")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+eBzYtdaY7Bc2ZDVl")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot1.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1430742022").split()))
