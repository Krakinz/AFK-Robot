"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""
import importlib
import time
import re
import sys
from termcolor import colored, cprint
from sys import argv
from typing import Optional
from HYPE_AFK_BOT import dispatcher, updater, LOGGER
from AWAY import ALL_MODULES
from MISCL import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, ChatMigrated, NetworkError, TelegramError, TimedOut, Unauthorized
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from MISCL.chat_status import *
AFKSAY = """—🚸••÷[Hყρҽ Aϝƙ Bσƚ]÷••🚸—
ᴡᴀɪᴛ ɪ ʜᴇᴀʀᴅ ᴛʜᴀᴛ ʏᴏᴜ ɴᴇᴇᴅᴇᴅ ꜱᴏᴍᴇᴛʜɪɴɢ ᴛʜᴀᴛ ᴡᴏᴜʟᴅ ꜱᴀʏ ᴛʜᴀᴛ ʏᴏᴜ ᴀʀᴇ ᴀꜰᴋ.
𝘞𝘦𝘭𝘭 𝘸𝘦𝘭𝘭 𝘞𝘦𝘭𝘭, 𝘥𝘰𝘯'𝘵 𝘺𝘰𝘶 𝘸𝘰𝘳𝘳𝘺.

ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʏᴘᴇ /afk ᴀɴᴅ ʀᴇꜱᴛ ɪꜱ ᴍʏ ᴡᴏʀᴋ.


🖥 Dҽʋ Mҽɳƚισɳ: @Krakinz | @KrakinzBot
—🚸••÷[ Hყρҽ Aϝƙ Bσƚ ]÷••🚸—
"""
HYPE_AFK_BOT_IMG = "https://telegra.ph/file/8e5be7f7bd1f93ef370b1.jpg"
IMPORTED = {}
HELPABLE = {}
GDPR = []

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("AWAY." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)


def start(update: Update, context: CallbackContext):
    if update.effective_chat.type == "private":
        update.effective_message.reply_photo(
            HYPE_AFK_BOT_IMG,
            AFKSAY,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="••÷  Add AFKBot to group  ÷••",
                    url="t.me/{}?startgroup=true".format(context.bot.username),)], ]),)
    else:
        update.effective_message.reply_photo(
            HYPE_AFK_BOT_IMG,
            "—🚸••÷[Hყρҽ Aϝƙ Bσƚ]÷••🚸—\n\n♦️𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓♦️\n𝘐 𝘩𝘢𝘷𝘦 𝘵𝘰 𝘣𝘦 𝘢𝘥𝘮𝘪𝘯 𝘪𝘯𝘰𝘳𝘥𝘦𝘳 𝘵𝘰 𝘸𝘰𝘳𝘬 𝘱𝘳𝘰𝘱𝘦𝘳𝘭𝘺.\n\n—🚸••÷[Hყρҽ Aϝƙ Bσƚ]÷••🚸—",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="••÷   🆅🅸🆂🅸🆃 ☆🍫 ÷••",
                    url="https://t.me/KrakinzBot")], ]),)


def main():
    start_handler = CommandHandler("start", start, run_async=True)
    dispatcher.add_handler(start_handler)


LOGGER.info("READY")
cprint(f"               —••÷[ Hყρҽ Aϝƙ Bσƚ ]÷••—    online", 'yellow')
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
main()
updater.idle()
cprint(f"—••÷[ Hყρҽ Aϝƙ Bσƚ ]÷••—    offline", 'white', 'on_red')
cprint(f"—🖥 Dҽʋ Mҽɳƚισɳ: ", 'red')
cprint(f"@Krakinz | @KrakinzBot", 'green')
updater.stop()
