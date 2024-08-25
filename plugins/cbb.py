from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>╭━━━━━━━━━━━━━━━➣\n┣⪼ Owner : <a href='tg://user?id={OWNER_ID}'>Him</a>\n┣⪼ Source : <a href'https://github.com/AniShin21/Shin-File-Bot.git'>Click Here</a>\n┣⪼ Language : <a href='https://www.python.org/'>Python</a>\n┣⪼ Library :<a href='https://docs.pyrogram.org/'>Pyrogram</a>\n┣⪼ Hosting :<a href='https://www.heroku.com/'>Heroku</a>\n╰───────────────⍟</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
                    ],
                    [
                        InlineKeyoardButton("Premium", callback_data="premium")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

elif data == "prenium":
    await query.message.edit_text(
        text=f"""
        Yo {first}{last}
        This Premium Feature Is About GitHub Repo--
        
        °You Will Get Token Verifaction On/Off
        
        °Add Premium User To Bot If Token Verifaction Is On
         Bot Will Not Let Premium User To Verify And Skip It
         
        °You Can Add Admins From Bot
        
        °If You Have Anime Bot Then You Will Get a Spicial Feature 
         /top, /weekly, /search <Anime Name> With These Commands
         """),
reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Return", callback_data="about")
        ]
    ]
)

        
