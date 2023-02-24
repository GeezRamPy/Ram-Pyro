# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram.helpers.PyroHelpers import ReplyCheck
from geezlibs.ram import pyram, ram
from config import CMD_HANDLER as cmd
from config import IG_ALIVE, CH_SFS, REPO_URL
from .help import add_command_help


@pyram("p", ram)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Anak Anjing!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@pyram("pe", ram)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@pyram("l", ram)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Kaum Dajal",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@pyram("el", ram)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@pyram("oi", ram)
async def salken(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Haii Salken Saya {client.me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("Kalian Anjing,Anak Haram Titisan Asmodeus, Bocah tengik, Penyembah tongkat Kera Sakti")


@pyram("ass", ram)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


@pyram("j", ram)
async def jakasem(client: Client, message: Message):
    xx = await edit_or_reply(message, "**Woi Kontol....**")
    await asyncio.sleep(3)
    await xx.edit("**Muka lo jelek Bgt Kaya kontol!!!🔥**")


@pyram("k", ram)
async def ngegas(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Hallo KIMAAKK SAYA {client.me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("**LU SEMUA NGENTOT 😂**")


@pyram("mutu", ram)
async def igehh(client: Client, message: Message):
    xx = await message.reply("**Mutualan IG Yuk!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih IG Ku = [TEKAN](https://instagram.com/{IG_ALIVE})", disable_web_page_preview=True)


@pyram("sfs", ram)
async def channel(client: Client, message: Message):
    xx = await message.reply("**Yok SFS!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih CH Ku = [TEKAN](https://t.me/{CH_SFS})", disable_web_page_preview=True)


@pyram("getstring", ram)
async def string(client: Client, message: Message):
    xx = await message.reply("**Jan Bawel!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih String = [TEKAN](https://t.me/geezRamStringroBot)", disable_web_page_preview=True)


@pyram("keluar", ram)
async def keluar(client: Client, message: Message):
    xx = await message.reply("`Processing...`")
    await asyncio.sleep(1)
    await xx.edit(f"{client.me.first_name} has left this group, bye!!")

