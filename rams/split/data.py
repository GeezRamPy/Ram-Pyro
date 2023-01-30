from pyrogram.types import InlineKeyboardButton, WebAppInfo

class Data:

    text_help_menu = (
        f"**《 Menu Inline RamPyro-Master 》\n╰┈➤ perintah: ? ! . * $ **"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("⇕ ʙᴜᴋᴀ ⇕", callback_data="reopen")]]
