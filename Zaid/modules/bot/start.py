from Zaid import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC
from pyrogram import filters, Client
from pyrogram.types import *
import asyncio

PHONE_NUMBER_TEXT = (
    "✘ Heya My Master👋!\n\n"
    "✘ I'm Your Assistant?\n\n"
    "‣ I can help you to host Your Left Clients.\n\n"
    "‣ This specially for Buzzy People's (lazy)\n\n"
    "‣ Use /generate to get Pyrogram String Session\n"
    "‣ Use /clone {string} to login client"
)

# ======================= START =======================

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
        [InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/fine_n_ok")],
        [InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/kryshupdate")],
    ]

    await client.send_photo(
        message.chat.id,
        ALIVE_PIC,
        caption=PHONE_NUMBER_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
    )

# ======================= STRING SESSION GENERATOR =======================

@app.on_message(filters.command("generate"))
async def generate_session(_, msg: Message):

    await msg.reply("📱 **Send Your Phone Number With Country Code**\nExample: `+919876543210`")

    phone = await app.listen(msg.chat.id)
    phone = phone.text

    client = Client("gen", api_id=API_ID, api_hash=API_HASH)

    await client.connect()

    try:
        code = await client.send_code(phone)
    except Exception as e:
        return await msg.reply(f"❌ Error: `{e}`")

    await msg.reply("📩 **Enter the OTP received:**\nFormat: `12345`")

    otp = await app.listen(msg.chat.id)
    otp = otp.text.replace(" ", "")

    try:
        await client.sign_in(phone, code.phone_code_hash, otp)
    except Exception:
        return await msg.reply("❌ OTP Invalid. Try Again.")

    string = await client.export_session_string()
    await client.disconnect()

    await msg.reply(f"✅ **Your Pyrogram String Session:**\n\n`{string}`\n\nKeep it safe!")

# ======================= CLONE =======================

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):

    try:
        session_string = msg.command[1]
    except:
        return await msg.reply("❌ Provide session string.\nExample: `/clone ABCDEF...`")

    text = await msg.reply("Booting Your Client...")

    try:
        client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
            plugins=dict(root="Zaid/modules")
        )

        await client.start()
        user = await client.get_me()

        await text.edit(
            f"✅ **Client Started Successfully As {user.first_name}**"
        )

    except Exception as e:
        await msg.reply(f"❌ ERROR: `{e}`")
