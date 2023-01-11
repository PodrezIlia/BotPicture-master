import modules.creating_buttons as m_buttons
import telebot

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.add(m_buttons.button_get_picture)