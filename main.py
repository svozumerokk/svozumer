import telebot as tb

TOKEN = "8519272723:AAEv4imQEvX6cPGtCfbSS9C_JVOCWpSAPGI"
bot = tb.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(msg):
    kb = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        tb.types.KeyboardButton("Русский"),
        tb.types.KeyboardButton("English")
    )
    bot.send_message(
        msg.chat.id,
        "Выберите язык / Choose language",
        reply_markup=kb
    )
@bot.message_handler(content_types=['text'])
def text_handler(msg):
    text = msg.text
    if text == "Русский":
        kb = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb.add("say HI!")
        bot.send_message(msg.chat.id, "Привет! Я бот-помощник 😊", reply_markup=kb)
    elif text == "English":
        kb = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb.add("say HI!")
        bot.send_message(msg.chat.id, "Hi! I'm your bot-helper 😊", reply_markup=kb)
    elif text == "say HI!":
        kb = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb.add("test1", "test2", "test3")
        bot.send_message(msg.chat.id, "Choose your question:", reply_markup=kb)
    elif text == "test1":
        bot.send_message(msg.chat.id, "Answer to test1")
    elif text == "test2":
        bot.send_message(msg.chat.id, "Answer to test2")
    elif text == "test3":
        bot.send_message(msg.chat.id, "Answer to test3")
    else:
        bot.send_message(msg.chat.id, "I don't understand 🤷")

# ===== run =====
bot.polling(none_stop=True)
