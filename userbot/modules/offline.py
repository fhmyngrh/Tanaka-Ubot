""" Userbot module which contains afk-related commands """
import asyncio
from datetime import datetime
from random import randint

from telethon.events import StopPropagation

from userbot.events import register

from userbot import (  # noqa pylint: disable=unused-import isort:skip
    AFKREASON,
    COUNT_MSG,
    CMD_HELP,
    ALIVE_NAME,
    ISAFK,
    BOTLOG,
    BOTLOG_CHATID,
    USERS,
    PM_AUTO_BAN,
)


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global afk_time
    global afk_start
    global afk_end
    not_afk = datetime.now()
    afk_end = not_afk.replace(microsecond=0)
    if ISAFK and mention.message.mentioned:
        now = datetime.now()
        afk_since = now - afk_time
        day = float(afk_since.seconds) // (24 * 3600)
        time = float(afk_since.seconds) % (24 * 3600)
        hours = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        if day == 1:
            afk_str = "Kemarin"
        elif day > 1:
            if day > 6:
                date = now + datetime.timedelta(
                    days=-day, hours=-hours, minutes=-minutes
                )
                afk_str = date.strftime("%A, %Y %B %m, %H:%I")
            else:
                wday = now + datetime.timedelta(days=-day)
                afk_str = wday.strftime("%A")
        elif hours > 1:
            afk_str = f"`{int(hours)}h{int(minutes)}m` Yang Lalu"
        elif minutes > 0:
            afk_str = f"`{int(minutes)}m{int(seconds)}s` Yang Lalu"
        else:
            afk_str = f"`{int(seconds)}s` Yang Lalu"

        is_bot = False
        if (sender := await mention.get_sender()) :
            is_bot = sender.bot
            if is_bot:
                return  # ignore bot

        chat_obj = await mention.client.get_entity(mention.chat_id)
        chat_title = chat_obj.title

        if mention.sender_id not in USERS or chat_title not in USERS:
            if AFKREASON:
                await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ `Karena    :` {AFKREASON}")
            else:
                await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ __Silahkan hubungi lagi nanti.__")
            if mention.sender_id is not None:
                USERS.update({mention.sender_id: 1})
            else:
                USERS.update({chat_title: 1})
        else:
            if USERS[mention.sender_id] % randint(2, 4) == 0:
                if AFKREASON:
                    await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ `Karena    :` {AFKREASON}")
                else:
                    await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ __Silahkan hubungi lagi nanti.__")
            if mention.sender_id is not None:
                USERS[mention.sender_id] += 1
            else:
                USERS[chat_title] += 1
        COUNT_MSG += 1

#Hi , Mau Maling Ya??        
#Xixixixi
#P o c o n g - U s e r b o t

@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    global afk_time
    global afk_start
    global afk_end
    not_afk = datetime.now()
    afk_end = not_afk.replace(microsecond=0)
    afk_str = "Beberap Saat Yang Lalu"
    if (
        sender.is_private
        and sender.sender_id != 777000
        and not (await sender.get_sender()).bot
    ):
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved

                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            afk_since = now - afk_time
            day = float(afk_since.seconds) // (24 * 3600)
            time = float(afk_since.seconds) % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if day == 1:
                afk_str = "Kemarin"
            elif day > 1:
                if day > 6:
                    date = now + datetime.timedelta(
                        days=-day, hours=-hours, minutes=-minutes
                    )
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-day)
                    afk_str = wday.strftime("%A")
            elif hours > 1:
                afk_str = f"`{int(hours)}h{int(minutes)}m` Yang Lalu"
            elif minutes > 0:
                afk_str = f"`{int(minutes)}m{int(seconds)}s` Yang Lalu"
            else:
                afk_str = f"`{int(seconds)}s` Yang Lalu"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ `Karena    :` {AFKREASON}")
                else:
                    await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ __Silahkan hubungi lagi nanti.__")
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ `Karena    :` {AFKREASON}")
                    else:
                        await mention.reply(f"**PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈\n❏ `Sejak     :` {afk_str}\n❏ __Silahkan hubungi lagi nanti.__")
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(outgoing=True, pattern="^.offline(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global afk_time
    global afk_start
    global afk_end
    afk_time = None
    afk_end = {}
    start1 = datetime.now()
    afk_start = start1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"┈──────────────────────┈\n❏ **PENGGUNA SEDANG OFFLINE**\n❏ `Karena    :` {AFKREASON}\n┈──────────────────────┈")
    else:
        await afk_e.edit("┈──────────────────────┈\n❏ **PENGGUNA SEDANG OFFLINE**\n┈──────────────────────┈")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#OFLINE\nKamu akan OFLINE!")
    ISAFK = True
    afk_time = datetime.now()
    raise StopPropagation
    
#Pocong - Userbot
#Ciee Hapus Credit
#Maling Aja Gapapa
#Port by @Pocongonlen

@register(outgoing=True, pattern="^.online(?: |$)(.*)", disable_errors=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global afk_time
    global afk_start
    global afk_end
    not_afk = datetime.now()
    afk_end = not_afk.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.edit("┈────────────────────┈\n❏ **PENGGUNA KEMBALI ONLINE** ❏\n┈────────────────────┈")
        await asyncio.sleep(3)
        await msg.delete()
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "Kamu menerima "
                + str(COUNT_MSG)
                + " pesan dari "
                + str(len(USERS))
                + " obrolan saat Anda pergi",
            )
            for i in USERS:
                if str(i).isnumeric():
                    name = await notafk.client.get_entity(i)
                    name0 = str(name.first_name)
                    await notafk.client.send_message(
                        BOTLOG_CHATID,
                        "["
                        + name0
                        + "](tg://user?id="
                        + str(i)
                        + ")"
                        + " sent you "
                        + "`"
                        + str(USERS[i])
                        + " message(s)`",
                    )
                else:  # anon admin
                    await notafk.client.send_message(
                        BOTLOG_CHATID,
                        "Admin anonim di `"
                        + i
                        + "` mengirimimu "
                        + "`"
                        + str(USERS[i])
                        + " pesan`",
                    )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None
# Pocong - Userbot
# Thanks for "Project Dark"
# Aji Kintil
# Xixixi Canda ji

CMD_HELP.update({
    "offline":
    "**Command :** `.offline` [Alasan]\
    \nUsage: Lakukan ketika ingin OFF.\nSiapapun Yang Balas, Tag, Atau Chat Kamu Mereka Akan Tau Alasan Kamu OFF.\
    \n\n**Command :** `.online`\
    \nUsage: Kembali Online"
})
