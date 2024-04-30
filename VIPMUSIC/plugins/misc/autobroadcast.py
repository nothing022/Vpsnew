import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else False


MESSAGE = f"""**ㅤㅤㅤ⚠️⚠️⚠️⚠️⚠️📡

❤️सबसे ज्यादा पैसा देने वाला Platform पूरी दुनिया को हिला के रख दिया MISS मत करना⭐️

✅MESSAGE  को INVITE करो और 3000 SE START से 50,000₹ रोज कमाओ

🫂Link:- https://t.me/PAISE_SE_PAISA_KAMAO  ✅"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⋆⏤‌ 𝗔ᴅ֟፝ؖ۬ᴅ 𝗠֟፝ؖ۬ᴇ 𝗬ᴏ֟፝ؖ۬ᴜʀ 𝗚ʀ֟፝ؖ۬ᴏᴜᴘ𓆩🔥𓆪", url=f"https://t.me/ll_RADHA_MUSICBOT?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGE

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=caption, reply_markup=BUTTON)
                    await asyncio.sleep(3)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 5000 seconds before next broadcast
        await asyncio.sleep(5000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
