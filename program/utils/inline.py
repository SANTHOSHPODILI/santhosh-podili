""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data=f'cls'),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="😯 sᴛᴏᴘ", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="😐 ᴘᴀᴜsᴇ", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="😶 ʀᴇsᴜᴍᴇ", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🥱 ᴍᴜᴛᴇ", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="😏 ᴜɴᴍᴜᴛᴇ", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="😁 ɴɪʙʙᴀ ᴄʟᴏsᴇ", callback_data='cls'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "😁 ɴɪʙʙᴀ ᴄʟᴏsᴇ", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "😇 ɴɪʙʙᴀ ʙᴀᴄᴋ", callback_data="cbmenu"
      )
    ]
  ]
)
