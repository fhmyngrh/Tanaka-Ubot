from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"β Berhasil Terkirim Ke {done} Group\nβ Gagal Mengirim Ke {er} Group")


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan beberapa teks untuk Siaran Global`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"β Berhasil Terkirim Ke {done} Obrolan\nβ Gagal Mengirim Ke {er} Obrolan")


CMD_HELP.update(
    {
        "broadcast": "πΎπ€π’π’ππ£π: `.gcast [Pesan]`\
         \nβ³ : Mengirim Pesan Group Secara Global.\
         \nπΎπ€π’π’ππ£π: `.gucast [Pesan]`\
         \nβ³ : Mengirim Pesan Pribadi Secara Global"
    }
)
