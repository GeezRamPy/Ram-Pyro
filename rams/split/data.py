from pyrogram.types import InlineKeyboardButton, WebAppInfo
from config import CMD_HANDLER as cmd

class Data:

    text_help_menu = (
        f"**◇ Menu Inline RamPyro-Master ◇\n╰☞Command Handler Mu adalah : {cmd}**"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("⇕ open menu ⇕", callback_data="reopen")]]
