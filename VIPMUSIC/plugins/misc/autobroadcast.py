import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else False


MESSAGE = f"""**๏𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐦𝐮𝐬𝐢𝐜 𝐩𝐥𝐚𝐲𝐞𝐫 𝐛𝐨𝐭 𝐟𝐨𝐫 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐠𝐫𝐨𝐮𝐩𝐬 +𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐯𝐜.🔥

🔥 𝐁𝐎𝐓-1 : [𝐑𝐀𝐃𝐇𝐀 𝐌𝐔𝐒𝐈𝐂](https://t.me/ll_RADHA_MUSICBOT)
🔥 𝐁𝐎𝐓-2 : [𝐐𝐔𝐄𝐄𝐍 𝐌𝐔𝐒𝐈𝐂](https://t.me/QUEEN_MUSIC_ROBOT)
🔥 𝐁𝐎𝐓-3 : [𝐒𝐓𝐀𝐑 𝐌𝐈𝐒𝐈𝐂](https://t.me/STAR_MUSICAL_BOT)
🔥 𝐎𝐖𝐍𝐄𝐑: [𝐎𝐖𝐍𝐄𝐑](https://t.me/ll_SARKAR_BABY_HU_ll)

➲ 𝐁𝐎𝐓 :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𓆩🔥𓆪𝐀𝐃𝐃 𝐌𝐄 𝐁𝐀𝐁𝐘𓆩🔥𓆪", url=f"https://t.me/ll_RADHA_MUSICBOT?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
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
                    await app.send_photo(chat_id, caption=caption, reply_markup=BUTTON)
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

        # Wait for 200 seconds before next broadcast
        await asyncio.sleep(200)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
