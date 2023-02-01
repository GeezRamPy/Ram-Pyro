# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import time
from datetime import datetime
import traceback
from sys import version as pyver
import os
import shlex
import textwrap
from typing import Tuple
import asyncio 

from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from rams.split.data import Data
from rams.split.inline import inline_wrapper, paginate_help
from config import ID_OWNER, BOT_VER, BRANCH as branch
from rams import CMD_HELP, StartTime, app

modules = CMD_HELP

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


async def alive_function(message: Message, answers):
    start = datetime.now()
    uptime = await get_readable_time((time.time() - StartTime))
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    msg = (
        f"☞ 𝗥𝗮𝗺𝗣𝘆𝗿𝗼-𝗕𝗼𝘁!!\n"
        f"☞ 𝗦𝗶𝗴𝗻𝗮𝗹: %sms\n"
        f"☞ 𝗨𝗽𝘁𝗶𝗺𝗲: </b> <code>{uptime}</code>" % (duration)
    )
    answers.append(
        InlineQueryResultArticle(
            title="Alive",
            description="Check Bot's Stats",
            thumb_url="https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("☬ 𝗠𝗮𝘀𝘁𝗲𝗿 ☬", url=f"tg://user?id={message.from_user.id}")]]
            ),
        )
    )
    return answers

async def ping_function(message: Message, answers):
    msg = (
        f"𝗥𝗮𝗺𝗣𝘆𝗿𝗼-𝗠𝗮𝘀𝘁𝗲𝗿 \n"
        "ㅤ⋙ sᴛᴀᴛᴜs : 𝗔𝗸𝘁𝗶𝗳!!! \n"
        f"ㅤㅤ⋙ ᴍᴏᴅᴜʟᴇs: </b> <code>{len(modules)} </code> \n"
        f"ㅤㅤ⋙ ᴠᴇʀsɪ ʙᴏᴛ: {BOT_VER} \n"
        f"ㅤㅤ⋙ ʙʀᴀɴᴄʜ: {branch} \n"
        f"ㅤㅤ⋙ ᴠᴇʀsɪ ᴘʏʀᴏ: </b> <code>{pyrover}</code>\n"
        f"ㅤㅤ⋙ ᴠᴇʀsɪ ᴘʏᴛʜᴏɴ: </b> <code>{pyver.split()[0]}</code>"
    )
    answers.append(
        InlineQueryResultArticle(
            title="rama",
            description="Check Bot's Stats",
            thumb_url="https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="༺ Oᴡɴᴇʀ ༻", url=f"tg://user?id={message.from_user.id}")]]
            ),
        )
    )
    return answers

async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            description="Check Command List & Help",
            thumb_url="https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers


@app.on_inline_query()
@inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alive":
            answerss = await alive_function(query, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
        elif string_given.startswith("rama"):
            answers = await ping_function(query, answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
