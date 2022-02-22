import telebot
import config
import sqlite3


try:
	con = sqlite3.connect('account.db')
	cursor = con.cursor()
	# users = cursor.execute("SELECT * FROM 'users'")
	# print(users.fetchall())
	# con.commit()
except sqlite3.Error as error:
	print('ошибка подключения sql', error)
finally:
	if con:
		con.close()




# first_simple_test_telegram_bot

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет")

# @bot.message_handlers(contxt_types=['text'])
# def lalala(message):
#     bot.send_message(message.chat.id, message.text)

bot.infinity_polling()