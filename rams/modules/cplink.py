import asyncio
import os
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client as gez
from pyrogram import Client
from geezlibs.ram.helpers.basic import *
from geezlibs.ram.helpers.PyroHelpers import *
from geezlibs.ram.utils.misc import *
from geezlibs.ram.utils.tools import *

#command takepm for forward to save message
@gez.on_message(filters.command("takepm", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def takepm(client: Client, message: Message):
    lol = message.reply_to_message
    if not lol:
       return await message.edit("**Please reply**")
    try:
       await lol.copy(message.from_user.id)
       await message.delete()
    except BaseException:
        pass
#command take for anu
@gez.on_message(filters.command("take", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def take(client: Client, message: Message):
    lol = message.reply_to_message
    if not lol:
       return await message.edit("**Please reply**")
    try:
       await lol.copy(message.chat.id)
       await message.delete()
    except BaseException:
        pass

#command fwd for forward
@gez.on_message(filters.command("fwd", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def fwd(client: Client, message: Message):
    lol = message.reply_to_message
    if not lol:
       return await message.edit("**Please reply**")
    try:
       await lol.forward(message.chat.id)
       await message.delete()
    except BaseException:
        pass
#command c for anu
@gez.on_message(filters.command("c", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def cp(client: Client, message: Message):
    tulis = get_arg(message)
    user = message.reply_to_message
    if not user:
       return await message.edit("lu goblok") 
    try:
       await user.copy(message.chat.id, caption=tulis)
    except Exception as e:
        return await message.edit(f"**ERROR** `{e}`")

#command cp for nyolong
@gez.on_message(filters.command("cp", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def kangcopy(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "Nyolong_lagi_bot"
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("userbotch")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Nyolong berhasil...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id)
        except BaseException:
            pass
        try:
            async for f in client.search_messages(message.chat.id, query="Trying to Download."):
                await f.delete()
            async for o in client.search_messages(message.chat.id, query="DOWNLOADING:"):
                await o.delete()
            async for g in client.search_messages(message.chat.id, query="Preparing to Upload!"):
                await g.delete()
        except BaseException:
            pass
