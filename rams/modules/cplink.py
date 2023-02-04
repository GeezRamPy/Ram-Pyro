import asyncio
import os
import time
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client as gez
from pyrogram import Client, filters, enums
from geezlibs.ram.helpers.basic import *
from geezlibs.ram.helpers.PyroHelpers import *
from geezlibs.ram.utils.misc import *
from geezlibs.ram.utils.tools import *

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@gez.on_message(filters.command("cp", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def kangcopy(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "Nyolong_lagi_bot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("userbotch")
            await client.join_chat("b4c0d")
            await client.join_chat("offsideaja")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mencuri...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id)
            await client.delete_message(bot, link)
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

@gez.on_message(filters.command("tt", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def kangtiktok(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "downloader_tiktok_bot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("userbotch")
            await client.join_chat("b4c0d")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mendownload...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id, caption="Powered by ©️ Geez|Ram")
            await client.delete_message(bot, link)
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

@gez.on_message(filters.command("ig", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def kangsosmed(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "thisvidbot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("userbotch")
            await client.join_chat("b4c0d")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mendownload...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=2):
                await c.copy(message.chat.id, caption="Powered by ©️ Geez|Ram")
            await client.delete_message(bot, link)
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

@gez.on_message(filters.command("pint", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def kangsos(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "saveasbot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("userbotch")
            await client.join_chat("b4c0d")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mendownload...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id, caption="Powered by ©️ Geez|Ram")
            await client.delete_message(bot, link)
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
# ==================================
#          LO NGENTOT
# ==================================
from pyrogram.types import Message
from geezlibs import logging
from geezlibs.ram.helpers.basic import edit_or_reply

@Client.on_message(filters.command("tonime", [".", "!", "?", ",", "$", "*"]) & filters.me)
async def convert_image(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("Please Reply to photo")
    if message.reply_to_message:
        await message.edit("processing ...")
        await logging(client)
    reply_message = message.reply_to_message
    photo = reply_message.photo.file_id
    bot = "qq_2d_ai_bot"
    await client.send_photo(bot, photo=photo)
    await asyncio.sleep(18)
    async for result in client.search_messages(bot, limit=1):
        if result.photo:
            await message.edit("uploading...")
            converted_image_file = await client.download_media(result)
            await client.send_photo(message.chat.id, converted_image_file, caption="Powered by ©️ Geez|Ram")
            await message.delete()
        else:
            await message.edit("error message ...")


@Client.on_message(filters.command("jurus", [".", "!", "?", ",", "$", "*"]) & filters.me)
async def deepfry(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("Reply Foto Untuk Mengedit")
    if message.reply_to_message:
        await message.edit("Gua bikin Jelek Fotolu nih!!!...")
        await logging(client)
    reply_message = message.reply_to_message
    photo = reply_message.photo.file_id
    bot = "image_deepfrybot"
    await client.send_photo(bot, photo=photo)
    await asyncio.sleep(3)
    async for result in client.search_messages(bot, limit=1):
        if result.photo:
            await message.edit("utiwiii maszehh...")
            converted_image_file = await client.download_media(result)
            await client.send_photo(message.chat.id, converted_image_file, caption="Powered by ©️ Geez|Ram")
            await message.delete()
        else:
            await message.edit("error message ...")


@Client.on_message(filters.command("kamui", [".", "!", "?", ",", "$", "*"]) & filters.me)
async def deepfry(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("Reply sticker Untuk Mengedit")
    if message.reply_to_message:
        await message.edit("Gua bikin Jelek sticker lu nih!!!...")
        await logging(client)
    reply_message = message.reply_to_message
    sticker = reply_message.sticker.file_id
    bot = "image_deepfrybot"
    await client.send_sticker(bot, sticker=sticker)
    await asyncio.sleep(3)
    async for result in client.search_messages(bot, limit=1):
        if result.sticker:
            await message.edit("sabaran...")
            converted_image_file = await client.download_media(result)
            await client.send_photo(message.chat.id, converted_image_file)
            await message.delete()
        else:
            await message.edit("error message ...")
