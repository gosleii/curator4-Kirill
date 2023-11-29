import telebot
bot = telebot.TeleBot('6954240802:AAGHDtNp6U0XxMD7AUC6Gu7UrwIvjfBvWPc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello World!')

@bot.message_handler(commands=['emptiness'])
def main(message):
    bot.send_message(message.chat.id, 'Пустота — есть форма')

@bot.message_handler(commands=['form'])
def main(message):
    bot.send_message(message.chat.id, 'Форма — есть пустота')

bot.infinity_polling()