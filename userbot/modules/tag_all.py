"""A Plugin to tagall in the chat for @UniBorg and cmd is `.all`"""

import asyncio
import random
import re

from userbot import CMD_HELP, bot
from userbot.events import register

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")
emoji = "😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🎲 🧩 ♟ 🎯 🎳 🎭💕 💞 💓 💗 💖 ❤️‍🔥 💔 🤎 🤍 🖤 ❤️ 🧡 💛 💚 💙 💜 💘 💝 🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧 🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍨".split(
    " "
)


@register(outgoing=True, pattern=".all(?: |$)(.*)"))
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()

        tags = list(
            map(
                lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        jumlah = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            jumlah.append(participant)

            if len(jumlah) == 5:
                tags = list(
                    map(
                        lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                        jumlah,
                    ),
                )
                jumlah = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(2)
    finally:
        FlagContainer.is_active = False
        
@register(outgoing=True, pattern=".mention(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    query = event.pattern_match.group(1)
    mentions = f"@all {query}"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100500):
        mentions += f"[\u2063](tg://user?id={x.id} {query})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)
    
@register(outgoing=True, pattern=".emojitag(?: |$)(.*)"))
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()

        tags = list(
            map(
                lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        current_pack = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            current_pack.append(participant)

            if len(current_pack) == 5:
                tags = list(
                    map(
                        lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                        current_pack,
                    ),
                )
                current_pack = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(2)
    finally:
        FlagContainer.is_active = False
        

CMD_HELP.update({
    'tagsall':
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.all [Text]`"
    "\n• : Untuk Mengetag semua anggota Maksimal 3.000 orang yg akan ditag di grup untuk mengurangi flood wait telegram."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mention`"
    "\n• : Untuk Menmention semua anggota yang ada di group tanpa menyebut namanya."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.emojitag`"
    "\n• : Untuk Mengetag semua anggota di grup dengan random emoji berbeda"
    "\n\n𝙉𝙤𝙩𝙚: Untuk Memberhentikan Tag ketik `.restart`"
})
