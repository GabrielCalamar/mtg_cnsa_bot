#https://github.com/eternnoir/pyTelegramBotAPI
import telebot
import random
from telebot import types

bot = telebot.TeleBot("935680230:AAEFtU7Ik2A7lWtRbjTJEbszRNRnYiZB9vA")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['plano'])
def send_plano(message):
	photo = open('/home/administrador/pypypy/Ejemplo.png', 'rb')
	bot.send_photo(message.chat.id, photo)
	#bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['play'])
def send_plano(message):
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('d6')
	itembtnv = types.KeyboardButton('Plano!')
	markup.row(itembtna, itembtnv)
	bot.send_message(message.chat.id, "Magia: El encuentro", reply_markup=markup)

@bot.message_handler(commands=['playV2'])
def send_plano(message):
	markup = types.ReplyKeyboardMarkup(row_width=1)
	itembtna = types.KeyboardButton('d6')
	itembtnv = types.KeyboardButton('Plano!')
	markup.add(itembtna, itembtnv)
	bot.send_message(message.chat.id, "Magia: El encuentro", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	res = message.text 
	if(message.text == "d6"):
		d = random.randint(1, 6)
		if(d == 1):
			res = "PLANESWALKER! ({})"
		elif(d == 6):
			res = "CAOS! ({})"
		else:
			res = "Nada. ({})"
		res = res.format(d)
	elif(message.text == "Plano!"):
		d = random.randint(1, 17)
		send_plano_d(message, d)
	
	if(message.text != "Plano!"):
		bot.reply_to(message, res)

def send_plano_d(message, d):
	img_path = "/home/administrador/pypypy/planos/png/{}.png"
	img_path = img_path.format(d)
	photo = open(img_path, 'rb')
	bot.send_photo(message.chat.id, photo)

bot.polling()