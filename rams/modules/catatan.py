
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.ram import pyram, ram
from rams import BOTLOG_CHATID
from rams.split.berak.SQL.notes_sql import add_note, get_note, get_notes, rm_note
from rams.modules.cplink import get_arg


@pyram("notes", ram)
async def list_notes(client, message):
    user_id = message.from_user.id
    notes = get_notes(str(user_id))
    if not notes:
        return await message.reply("Tidak ada catatan.")
    msg = f"Daftar catatan\n"
    for note in notes:
        msg += f"* {note.keyword}\n"
    await message.reply(msg)


@pyram("dlt", ram)
async def remove_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    if rm_note(str(user_id), notename) is False:
        return await message.reply(
            "Tidak dapat menemukan catatan: {}".format(notename)
        )
    return await message.reply("Berhasil Menghapus Catatan: {}".format(notename))


@pyram("save", ram)
async def simpan_note(client, message):
    keyword = get_arg(message)
    user_id = message.from_user.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("Tolong balas ke pesan")
    anu = await msg.forward(BOTLOG_CHATID)
    msg_id = anu.id
    await client.send_message(
        BOTLOG_CHATID,
        f"#NOTE\nKEYWORD: {keyword}"
        "\n\nPesan berikut disimpan sebagai data balasan catatan untuk obrolan, mohon JANGAN dihapus !!",
    )
    await sleep(1)
    add_note(str(user_id), keyword, msg_id)
    await message.reply(f"Berhasil menyimpan note {keyword}")


@pyram("get", ram)
async def panggil_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    note = get_note(str(user_id), notename)
    if not note:
        return await message.reply("Tidak ada catatan seperti itu.")
    msg_o = await client.get_messages(BOTLOG_CHATID, int(note.f_mesg_id))
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)

