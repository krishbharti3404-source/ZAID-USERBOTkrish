import time
import asyncio
from datetime import datetime
import speedtest
from pyrogram import Client, filters
from pyrogram.types import Message

from Zaid import StartTime, app, SUDO_USER
from Zaid.helper.PyroHelpers import SpeedConvert
from Zaid.modules.bot.inline import get_readable_time
from Zaid.modules.help import add_command_help


class WWW:
    SpeedTest = (
        "⚡ **Speedtest Results** ⚡\n\n"
        "📅 **Started at:** `{start}`\n\n"
        "🏓 **Ping:** `{ping} ms`\n"
        "⬇️ **Download:** `{download}`\n"
        "⬆️ **Upload:** `{upload}`\n"
        "🌐 **ISP:** __{isp}__"
    )


@Client.on_message(
    filters.command(["speedtest"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
        await message.delete()
    except:
        pass

    spd = speedtest.Speedtest()

    await new_msg.edit("`Finding best server...`")
    spd.get_best_server()

    await new_msg.edit("`Testing download speed...`")
    spd.download()

    await new_msg.edit("`Testing upload speed...`")
    spd.upload()

    await new_msg.edit("`Getting results...`")
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")

    try:
        await message.delete()
    except:
        pass

    # Animation
    for p in [20, 40, 60, 80, 100]:
        await xx.edit(f"**{p}%** {'█' * (p // 10)}{'▒' * (10 - (p // 10))}")
        await asyncio.sleep(0.1)

    end = datetime.now()
    duration = (end - start).microseconds / 1000

    OWNER_USERNAME = "@Nonsexcy"  # 🔥 Replace with your actual username if needed

    await xx.edit(
        f"❏ **𝗣𝗢𝗡𝗚™**\n"
        f"├• **ᴘɪɴɢ:** `{duration} ms`\n"
        f"├• **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"├• **ᴏᴡɴᴇʀ:** {OWNER_USERNAME}\n"
        f"└• **ᴜꜱᴇʀ:** {client.me.mention}"
    )


add_command_help(
    "ping",
    [
        ["ping", "Check if bot is alive — shows ping, uptime & owner info."],
        ["speedtest", "Run an internet speed test and show full results."],
    ],
)
