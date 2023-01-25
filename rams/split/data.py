from pyrogram.types import InlineKeyboardButton, WebAppInfo
from config import CMD_HANDLER as cmd

class Data:

    text_help_menu = (
        f"**《 Menu Inline RamPyro-Master 》\n╰┈➤perintah: {cmd}**"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("⇕ ʙᴜᴋᴀ ⇕", callback_data="reopen")]]
