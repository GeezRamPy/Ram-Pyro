from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram.helpers.PyroHelpers import ReplyCheck



@Client.on_message(filters.command(["sholawat", "saw"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    ram = await message.reply("`Tunggu Sebentar...`")
    await gather(
        ram.delete(),
        client.send_audio(
            message.chat.id,
            choice(
                [
                    sholawat.audio.file_id
                    async for asupan in client.search_messages(
                        "sholawatcintanabi", filter=enums.MessagesFilter.AUDIO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command(["alquran", "alq"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    ram = await message.reply("`Tunggu Sebentar...`")
    await gather(
        ram.delete(),
        client.send_voice(
            message.chat.id,
            choice(
                [
                    alquran.voice.file_id
                    async for asupan in client.search_messages(
                        "Alquran_voicee", filter=enums.MessagesFilter.VOICE
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
