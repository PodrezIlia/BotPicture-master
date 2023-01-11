import modules.creating_bot as m_bot
import modules.file_search_path as m_path
import modules.creating_inline_keyboard as m_inline_keyboard

def send_message_user(message):
    if message.text.lower() == "get picture":
        path_file = m_path.path_search("images/1.jpeg")
        m_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Повітряна куля",
            reply_markup= m_inline_keyboard.inline_keyboard
        )
    