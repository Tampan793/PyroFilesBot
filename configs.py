# (c) @M4SK3R1N

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
Ini adalah Bot Toko Berkas Permanen!
Kirimi saya file apa pun, saya akan menyimpannya di Database saya. Juga berfungsi untuk saluran. Tambahkan saya ke saluran sebagai Admin dengan Izin Edit, saya akan menambahkan Simpan File Unggahan di Saluran & tambahkan Tautan Tombol yang Dapat Dibagikan.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})
📝 **Language:** [Python3](https://www.python.org)
📚 **Library:** [Pyrogram](https://docs.pyrogram.org)
📡 **Hosted on:** [Heroku](https://heroku.com)
🕷️ **Developer:** @M4SK3R
👥 **Support Group:** [Linux Repositories](https://t.me/M4SK3R1N)
📢 **Updates Channel:** [Discovery Projects](https://t.me/ViralTwitterHot)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @M4SK3R

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://t.me/M4SK3R) ( Anything )
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
