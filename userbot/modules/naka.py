from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.naka(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Muka Lo Kaya Babi๐**")
    sleep(1)
    await typew.edit("**Ehh Gak Bercanda Deh๐**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Muka Lo Kaya Babi๐**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh, Lo Cakep Kaya Artis Korea๐**")
    sleep(1)
    await typew.edit("**TAPI BOONG ๐**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Lo Nangis Minta Balon๐**")
    sleep(1)
    await typew.edit("**Maaf Ya Naka Ganteng Bercanda๐**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")
# Create by myself @localheart

CMD_HELP.update({
    "naka":
    "๐พ๐ค๐ข๐ข๐๐ฃ๐: `.naka`\
    \nโณ : Coba ae."
})
