import telebot as tb
bot = telebot.TeleBot('8519272723:AAEv4imQEvX6cPGtCfbSS9C_JVOCWpSAPGI')
@bot.message_handler(commands=['start'])
def start(msg):
    mup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = tb.types.KeyboardButton("Русский")
    btn2 = tb.types.KeyboardButton("English")
    mup.add(btn, btn2)
    bot.send_message(msg.from_user.id, "Выберите язык / Choose language", reply_markup=mup)

@bot.message_handler(commands=['start'])
def start(msg):
    mup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = tb.types.KeyboardButton("say HI!")
    mup.add(btn1)
    bot.send_message(msg.from_user.id, "HI! Im ur bot-helper!", reply_markup=mup)
@bot.message_handler(commands=['text'])
def text(msg):
    #if msg.text == 'say HI!':
    mup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = tb.types.KeyboardButton("test1")
    btn2 = tb.types.KeyboardButton("test2")
    btn3 = tb.types.KeyboardButton("test3")
    mup.add(btn1,btn2,btn3)
    bot.send_message(msg.from_user.id, "Choose ur question", reply_markup=mup)
    if msg.text == 'test1':
        bot.send_message(msg.from_user.id, "a2test1", parse_mode='Markdown')
    elif msg.text == 'test2':
        bot.send_message(msg.from_user.id, 'a2test2', parse_mode='Markdown')
    elif msg.text == 'test3':
        bot.send_message(msg.from_user.id, 'a2test3', parse_mode='Markdown')

@bot.message_handler(commands=['switch'])
def switch(msg):
    mup = tb.types.InlineKeyboardMarkup()
    switchb = tb.types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
    mup.add(switchb)
    
@bot.message_handler(commands=['callback'])
def callback(msg):
    import datetime
    now = datetime.datetime.now()
    cid = msg.chat.id()
    date = (now.year,now.month)
    csd[cid] = date
    mup = cc(now.year,now.month)
    bot.send_message(msg.chat.id, "please, choice date", reply_markup=mup)
    bot.answer_callback_query(call.id, text="date is choiced")
    
bot.polling(none_stop=True, interval=0)
