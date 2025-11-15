import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from KRISHUSERBOT import app  # <-- change this according to your bot's main file

API_ID = 123456   # <-- apna api id daalna
API_HASH = "your_api_hash"  # <-- apna api hash daalna


# STEP 1 - PHONE NUMBER INPUT
@app.on_message(filters.command("genstring") & filters.private)
async def gen_string_start(bot, message: Message):
    await message.reply("📲 **Apna Phone Number bhejo:**\nFormat: +91xxxxxxxxxx")

    response = await bot.listen(message.chat.id, timeout=60)
    phone = response.text

    client = Client(
        name="gen_session",
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=True
    )

    await client.connect()

    try:
        sent = await client.send_code(phone)
        await message.reply("📩 **OTP aa gaya hoga!**\n\n**OTP bhejo:**\nFormat: `12345`")
    except Exception as e:
        await message.reply(f"❌ Error: `{e}`")
        return

    # STEP 2 - OTP INPUT
    otp = await bot.listen(message.chat.id, timeout=60)
    otp_code = otp.text.replace(" ", "")

    try:
        await client.sign_in(phone, sent.phone_code_hash, otp_code)
    except Exception as e:
        await message.reply(f"❌ Error (OTP): `{e}`")
        return

    # STEP 3 - STRING EXPORT
    try:
        string = await client.export_session_string()
        await message.reply(
            "**✅ STRING SESSION GENERATED SUCCESSFULLY!**\n\n"
            f"```\n{string}\n```"
        )
    except Exception as e:
        await message.reply(f"❌ Error (generate): `{e}`")

    await client.disconnect()
