# (c) @M4SK3R1N

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "6118254"))
	API_HASH = os.environ.get("API_HASH", "7f31b2fa35dde921ddd87895b3de5500")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "1844285172:AAGWEu0_6PbSHAPlNVmqoimptEFItQTi0N4")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "ViralTwitterHotBot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001593816516"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1710132981"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Kemek:Waaoo123@cluster0.ptjnj.mongodb.net/cluster0?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001507080304")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001523314599")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	ABOUT_BOT_TEXT = f"""
Ini adalah Bot Toko Berkas Permanen!
Kirimi saya file apa pun, saya akan menyimpannya di Database saya. Juga berfungsi untuk saluran. Tambahkan saya ke saluran sebagai Admin dengan Izin Edit, saya akan menambahkan Simpan File Unggahan di Saluran & tambahkan Tautan Tombol yang Dapat Dibagikan.

🤖 **My Name:** [Bot File](https://t.me/{BOT_USERNAME})
🕷️ **Developer:** @xH4X0Rx
👥 **Support Group:** [Coming Soon]
📢 **Updates Channel:** [F for Respect](https://t.me/TiktokViral18Plus_Pemersatu)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @xH4X0Rx

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.
Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.
[Donate Now](https://t.me/M4SK3R) ( Anything )
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Restored Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
