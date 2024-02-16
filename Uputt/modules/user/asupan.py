from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from Uputt.helpers.basic import edit_or_reply
from Uputt.helpers.PyroHelpers import ReplyCheck

from .help import *


@Client.on_message(filters.command(["asupan", "ptl"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    Uputt = await edit_or_reply(message, "`Tunggu Sebentar...`")
    await gather(
        Uputt.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

@Client.on_message(filters.command(["bokep"], cmd) & filters.me)
async def _(client, message):
    y = await message.reply("<b>🔍 Mencari Video Bokep...</b>")
    try:
        await client.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except BaseException:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(
            message.chat.id,
            caption=f"<b>Bokep By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>")
    if client.me.id == 1637576534:
        return
    await client.leave_chat(-1001867672427)

# WARNING PORNO VIDEO THIS !!!



@Client.on_message(filters.command(["ayang"], cmd) & filters.me)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Ayangnya [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@Client.on_message(filters.command(["ppcp", "couple"], cmd) & filters.me)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple nya Nih Kak",
    )

    await yanto.delete()

@Client.on_message(filters.command(["joe", "joko"], cmd) & filters.me)
async def joe(client, message):
    yanto = await message.reply("🔎 `mencari jodoh joe...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply("😂",)

    await yanto.delete()

@Client.on_message(filters.command(["sad", "anu"], cmd) & filters.me)
async def joe(client, message):
    yanto = await message.reply("🔎 `mencari anu...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply("LAGI LATIHAN BIAR KUAT MELIHAT DIA SAMA YANG LAIN",)
    await yanto.delete()

@Client.on_message(filters.command(["ppanime"], cmd) & filters.me)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Anime nya Nih Kak",
    )

    await yanto.delete()


add_command_help(
    "asupan",
    [
        [
            f"asupan atau {cmd}ptl",
            "Untuk Mengirim video asupan secara random.",
        ],
        [
            f"ayang {cmd}",
            "Untuk Mencari Foto Ayang Secara Random.",
        ],
        [
            f"ppcp atau {cmd}couple",
            "Untuk Mencari Pp Couple Secara Random.",
        ],
        [
            f"ppanime {cmd}",
            "Untuk Mencari Pp Anime Secara Random.",
        ]
    ],
)
