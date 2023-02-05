from pyrogram.types import InlineKeyboardButton, WebAppInfo
from rams import CMD_HELP
modules = CMD_HELP
class Data:

    text_help_menu = (
        f"**Menu Inline Ram-Pyro**\n**Perintah :** ? ! . * , $"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("⇕ ʙᴜᴋᴀ ⇕", callback_data="reopen")]]
