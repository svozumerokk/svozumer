import telebot as tg
from telebot import types
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


BOT_TOKEN = 'nope'
bot = tg.TeleBot(BOT_TOKEN)

BUTTON_TEST1 = "test1"
BUTTON_TEST2 = "test2"
BUTTON_TEST3 = "test3"
ANSWERS = {
    BUTTON_TEST1: "Answer to test1",
    BUTTON_TEST2: "Answer to test2",
    BUTTON_TEST3: "Answer to test3"
}


def create_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(BUTTON_TEST1, BUTTON_TEST2, BUTTON_TEST3)
    return keyboard


@bot.message_handler(commands=['start', 'help'])
def start(msg):
    try:
        bot.send_message(
            msg.chat.id,
            "Choose your question:",
            reply_markup=create_main_keyboard()
        )
        logger.info(f"User {msg.from_user.id} started the bot")
    except Exception as e:
        logger.error(f"Error in start handler: {e}")


@bot.message_handler(func=lambda message: True)
def handle_message(msg):
    try:
        text = msg.text
        if text in ANSWERS:
            bot.send_message(msg.chat.id, ANSWERS[text])
            logger.info(f"User {msg.from_user.id} selected: {text}")
        else:
            bot.send_message(
                msg.chat.id,
                "I don't understand 🤷\nPlease use the buttons below."
            )
            logger.warning(f"Unknown message from {msg.from_user.id}: {text}")
    
    except Exception as e:
        logger.error(f"Error in message handler: {e}")
        bot.send_message(msg.chat.id, "An error occurred. Please try again.")


def main():
    logger.info("Bot is starting...")
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Critical error: {e}")


if __name__ == "__main__":
    main()
