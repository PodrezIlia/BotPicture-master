import telebot
inline_bt1 = telebot.types.InlineKeyboardButton(text= "Замовити", callback_data = "замовити")
inline_bt2 = telebot.types.InlineKeyboardButton(
    text= "Перейти до сайту", 
    url = "https://akspic.ru/album/best_wallpapers"
)