from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import BOT_USERNAME
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery



@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Group Music Bot : Help Menu**

__Γ First Add Me To Your Group..
Γ Promote Me As Admin In Your Group With All Permission..__

**π· Common Commands For [Starz Music Bot](https://t.me/starz_bots).

β’ `/play`<song name> - To play song from. YouTube 
β’ `/audio` - Reply to audio file/YouTube link to play
β’ `/pause` - To pause currently stream
β’ `/resume` - To resume currently paused
β’ `/skip` or `/next` - to change song(work only  if another song is in queue) 
β’ `/end` or `/stop` - stop/ends music Stream
β’ `/refresh` or `/restart` - to restart Bot Server(only for heroku)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ποΈ Support Group ποΈ", url="https://t.me/Starz_SUPPORT"),
                    InlineKeyboardButton(text="π£ Channel", url=f"https://t.me/starz_Bots")
                ],
                [
                    InlineKeyboardButton(
                        "π‘ BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""<b>π πππππ πππππ β ππππΎπππ ππ ππ π½πππ

ππππ ππ πΌ π½ππ πΏπππππππΏ ππ πππΌπ πππππΎ ππ ππππ ππππππ!

ππππ πΌππ ππππ πΎππΏπ ππ πππ ππππ π½ππ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βSummon Meβ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)
                  ],[
                    InlineKeyboardButton(
                       "π£οΈ Support π£οΈ", url="https://t.me/starz_support"
                    ),
                    InlineKeyboardButton(
                        "π£ Updates π£", url="https://t.me/starz_Bots")
                ],[
                    InlineKeyboardButton(
                        "π Commands", callback_data="cbcmds"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
