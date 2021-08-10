from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name
from userbot import CMD_HELP
from userbot.events import register


@register(pattern=".tag(on|off|all|bots|rec|admins|owner)?(.*)",
          outgoing=True, groups_only=True)
async def _(e):
    okk = e.text
    msg = e.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    if msg:
        mention = f"{msg}\n\n"
    else:
        mention = ""
    async for bb in e.client.iter_participants(e.chat_id, 99):
        users = users + 1
        x = bb.status
        y = bb.participant

        if isinstance(x, onn):
            o = o + 1
            if "on" in okk:
                mention += f"[{get_display_name(bb)}](tg://user?id={bb.id}) "

        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    mention += f"[{get_display_name(bb)}](tg://user?id={bb.id}) "

        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    mention += f"[{get_display_name(bb)}](tg://user?id={bb.id}) "

        if isinstance(y, owner):
            if "admin" or "owner" in okk:
                mention += f"✰ [{get_display_name(bb)}](tg://user?id={bb.id}) ✰ "

        if isinstance(y, admin):
            if "admin" in okk:
                if not bb.deleted:
                    mention += f"[{get_display_name(bb)}](tg://user?id={bb.id}) "

        if "all" in okk:
            if not (bb.bot or bb.deleted):
                mention += f"[{get_display_name(bb)}](tg://user?id={bb.id}) "

        if "bot" in okk:
            if bb.bot:
                mention += f"[{get_display_name(bb)}](tg://user?id={bb.id}) "
    await e.client.send_message(e.chat_id, mention)
    await e.delete()


CMD_HELP.update({
    'tags':
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tagall`"
    "\n• : Tag Top 100 Members of chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tagadmin`"
    "\n• : Tag Admins of that chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tagowner`"
    "\n• : Tag Owner of that chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tagbot`"
    "\n• : Tag Bots of that chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tagrec`"
    "\n• : Tag recently Active Members."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tagon`"
    "\n• : Tag online Members(work only if privacy off)."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tagoff`"
    "\n• : Tag Offline Members(work only if privacy off)."
})
