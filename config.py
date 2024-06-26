import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29581926"))
API_HASH = getenv("API_HASH", "845b0f276375ac7bd2ced570290b3e26")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6111967692:AAFEXQo6_5LyA9GNJz-m233iS_57eWr1aBk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kalpanapreethiney:Ez4Xke7VUm4VQFAr@cluster0.hsx1cck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001975396715"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "1556830659"))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "15"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TeamInflex/InflexMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TeamInflex")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/InflexSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", "BQHDYmYAQuwq_9gm087Bf5LLsCgBOeWvIq572FhNtyXnmLQzaQuICNDAsqeR3-MhPEgEFkF0l2opHA5P1hb5nx462qZSOmU8L2BOMCEZTMP7BY9ycI-t__YyuW8aweIZpa5uCK2I-MqiwxdtoxORQIh3zKNeL3NVT6jAGPCFqIsfSV0RcP8ePC3fYCC5eY-B8g9nCkI8oxKudVHJQSuzAJ98uGHKhAqNQ2nHCaQI7SPTSHS7OAlbZ4Of3elIZEkzXOw6RAPrkAkKHR7AGRYMWgZDhtoRiHekKOB3ewfIChVMIEkkwCMGNbLCYElZ522xJdu0RbsfEHQpJudCt-0dvffRLsftQAAAAAGw3CIDAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://telegra.ph/file/698ce38fdd209887f85ff.jpg"]
PING_IMG_URL = ["https://telegra.ph/file/8553b61c381016f0bf7d8.jpg"]
STATS_IMG_URL = ["https://telegra.ph/file/8f4293af18fdb472c7cfe.jpg"]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/f72ea4bd955c418c724e1.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://telegra.ph/file/5547c6a0bcfc016089088.png"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
