import telebot
from telebot import types
import sqlite3
import random
import threading
import time
import schedule


token = os.environ.get('bot_token')
idme = os.environ.get('me_ids')

bot = telebot.TeleBot(token);
ids = idme

rand_no0 = '★'
rand_yes0 = '★★'
rand_all = '★★★'
def job():
	#print("I'm leaning")
	dict['S'] = 'жду'
	markup1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup1.row(rand_no0 , rand_yes0 , rand_all)
	bot.send_message(ids, 'Hello', reply_markup=markup1)

def pop():
	#print("I'm")
	if dict['S'] == 'жду' :
		#print('Ты не успел!!!1')
		dict['S'] = 'есть'

# while True:
#     # run_pending
#     schedule.run_pending()
#     time.sleep(10)


dict = {'S': 'есть'}
def my_timer(print_interval):
	
	data = threading.local()
	data.counter = 1

	schedule.every().day.at("22:00").do(job)
	schedule.every().day.at("23:59").do(pop)

	while True:
		schedule.run_pending()
		#schedule.every(3).seconds.do(pop)
		#pop()
		
		time.sleep(print_interval)
		#print('work')
		if dict['S'] == 'есть' :
			pass
		elif dict['S'] == 'нет':
			dict['S'] = 'есть'
			#print('НО КАК БЫ НЕТ')
		elif dict['S'] == 'да':
			dict['S'] = 'есть'
			#print('ДА КАК БЫ ДА')
		# 	#markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		# 	#markup.row(rand_no0 , rand_yes0)
		# 	markup = telebot.types.InlineKeyboardMarkup()
		# 	markup.add(telebot.types.InlineKeyboardButton(text=buy, callback_data=buy))
		# 	markup.add(telebot.types.InlineKeyboardButton(text=ball, callback_data=ball))
		# 	bot.send_message(user_id, "Час прошёл , готов работать?", reply_markup=markup)
		# 	break

t = threading.Thread(target=my_timer, name="My time thread", args=(10, ), daemon=True)
t.start()



# conn = sqlite3.connect('zero.db', check_same_thread=False)
# cursor = conn.cursor()



#buy = 'Магазин'
#ball = 'Баланс'
### fd9c9c4d931450535a01d04e2316be99
#but_list = ['One', 'Two', 'Three']

#rand = random.choice(but_list)
#dict = {'user_id': 0}
# @bot.message_handler(commands=['start'])
# def start_message(message):                                     # 

# 	user_id = message.chat.id
# 	dict['user_id'] = user_id
	
# 	try:
# 		cursor.execute("INSERT INTO 'subscriptions'  ('user_id','ballance') VALUES(?,?)", (user_id,0))		
# 	except:
# 		pass
# 	conn.commit()

	# markup = telebot.types.InlineKeyboardMarkup()
	# markup.add(telebot.types.InlineKeyboardButton(text=buy, callback_data=buy))
	# markup.add(telebot.types.InlineKeyboardButton(text=ball, callback_data=ball))

	# bot.send_message(user_id , 'ПриветSS' , reply_markup=markup)

#print(user_id)
#user_id = 0
#user_id = dict['user_id']
#user_id = dict['user_id']

@bot.message_handler(func=lambda message: rand_yes0 , content_types=['text'])
def process_step(message):
	if message.text == rand_yes0 :                                      # Если Да.
		dict['S'] = 'да'
		#print('YES')
	
	elif message.text == rand_no0:                                      # Если Нет.
		dict['S'] = 'нет'
		#print('NO')
		# Кнопки sleep
	elif message.text == rand_all:                                      # Если Нет.
		dict['S'] = 'да'
		#print('NO')

# @bot.callback_query_handler(func=lambda call: True)
# def query_handler(call):

# 	#bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
# 	element = cursor.fetchone()
# 	answer = ''
# 	if call.data == buy:
# 		answer = 'Окей , напишу тебе через '
# 		bot.send_message(call.message.chat.id, answer)

# 		#cursor.execute("SELECT * FROM subscriptions WHERE user_id = ?" , (user_id,))
# 		#item = cursor.fetchall()
# 		#print(item)
# 		#item_id = item[1]
# 		user_id = dict['user_id']
# 		cursor.execute("UPDATE subscriptions SET ballance = 200 WHERE user_id = ? ", (user_id,))
		
# 		conn.commit()
# 	elif call.data == ball:
# 		answer = 'Окей , напишу тебе через 3 минуты , ну или если ты сам управишься пораньше?'
# 		bot.send_message(call.message.chat.id, answer)
# 		user_id = dict['user_id']
# 		cursor.execute("UPDATE subscriptions SET ballance = 100 WHERE user_id = ? ", (user_id,))
# 		conn.commit()
# 	else:
# 		answer = 'Окей'
# 		bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True, interval=0)