import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28137343"))
    API_HASH = os.environ.get("API_HASH", "fe750c46d5746643392aa2edda2068f6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5139083086:AAHnXqQvMNsnfv4qkl8gqLPpcgX5sDRFISs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOL4Bu7694CJAzh9yF7ewX1SPHxs9hYJdPduQ2k4QyjZU5BE0idYcrrbS9wLKjCCOKAzd8EindP9whMLovN9S91fWp0EC8UdYFghU8zHqyCxF4An3fcmHR5iPtImEnHCWzZYdtASC-QMEZfAyBkAnv04RLhiKLxzp2ya2w6tT5MpO2BTAy6SyJ-L5DIfKu_N5MO6F9_aYPOEvMlkF2UG8As7KY_78pGlTUtRlXMBuftA_uoxdJYkOjAfHg5sa5yZTS37Op9KB4lVRMs-hxn_4tu4TTUEMSZcGWgLoFHakdyz2YuZDTVnibifN010jBm6zUXKBcf3t3nsg6I-rO8Wu_WWM7I4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "a1HDmovieDK_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1898724016")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
