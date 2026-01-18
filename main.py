import telebot as tg
import logging
logging.basicConfig(level=logging.INFO)

bot = tg.TeleBot('8НЕТ')
#@bot.message_handler(commands=['start'])
#def start(msg):
#    kb = tg.types.ReplyKeyboardMarkup(resize_keyboard=True)
#    kb.add(
#        tg.types.KeyboardButton("Русский"),
#        tg.types.KeyboardButton("English")
#    )
#    bot.send_message(
#        msg.chat.id,
#        "Выберите язык / Choose language",
#        reply_markup=kb
#    )
@bot.message_handler(commands=['start'])
def start(msg):
    kb = tg.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("test1", "test2", "test3")
    bot.send_message(msg.chat.id, "Choose your question:", reply_markup=kb)

@bot.message_handler(func=lambda message: True)
def hmsg(msg):
    text = msg.text
    if text == "test1":
        bot.send_message(msg.chat.id, "Answer to test1")
    elif text == "test2":
        bot.send_message(msg.chat.id, "Answer to test2")
    elif text == "test3":
        bot.send_message(msg.chat.id, "Answer to test3")
    elif text == "/start":
        start(msg)
    else:
        bot.send_message(msg.chat.id, "I don't understand 🤷")

if __name__ == "__main__":
    bot.polling(none_stop=True)
    print('Bot started...')
