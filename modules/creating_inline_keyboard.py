import telebot
import modules.creating_inline_button as m_inline_bt
inline_keyboard = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard.add(m_inline_bt.inline_bt1, m_inline_bt.inline_bt2)