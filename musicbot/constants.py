import os.path

MAIN_VERSION = '1.9.5_2'
SUB_VERSION = ''
VERSION = MAIN_VERSION + SUB_VERSION

AUDIO_CACHE_PATH = os.path.join(os.getcwd(), 'audio_cache')
DISCORD_MSG_CHAR_LIMIT = 2000

# Change based on where you send the POST request to
WEBHOOK_URL = "http://127.0.0.1:5000/webhook"
