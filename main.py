''' Подключение бибилиотек '''
import telepot, os, time, json
from pathlib import Path
from telepot.loop import MessageLoop


''' Подключение файла send_message для работы с сообщениями '''
import send_message

''' Ввод токена бота (вместо BOT_TOKEN) '''
bot_token = ("BOT_TOKEN")
bot = telepot.Bot(bot_token)
USER_LIST = ('userlist.json')

''' Метод для текстовых сообщений '''
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == ('text') and int(chat_id) == int(msg['from']['id']) :

		cmd = str(msg['text'])
		from_id = str(msg['from']['id'])
		from_name = str(msg['from']['first_name'])

		if (cmd == ('/start') or cmd == ('/restart')):

			path = Path(USER_LIST)
			temp = json.loads(path.read_text(encoding='utf-8'))

			if str(chat_id) not in temp["userlist"]:
				temp["userlist"].append(str(from_id))
				path.write_text(json.dumps(temp,sort_keys=True, indent=4, separators=(',', ': ')), encoding='utf-8')

			send_message.build_message(bot, from_id, ('start'))

''' Метод для ответов на кнопки '''
def callback_response(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor = 'callback_query')
	bot.answerCallbackQuery(query_id)
	bot.deleteMessage(telepot.message_identifier(msg['message']))

	if query_data == ('/getMovies'):

		send_message.build_message(bot, from_id, ('getMovies'))
		return

	elif query_data == ('/horror'):
		send_message.build_message(bot, from_id, ('horror'))
		return

	elif query_data == ('/drama'):
		send_message.build_message(bot, from_id, ('drama'))
		return

	elif query_data == ('/action'):
		send_message.build_message(bot, from_id, ('action'))
		return

	elif query_data == ('/comedy'):
		send_message.build_message(bot, from_id, ('comedy'))
		return

	elif query_data == ('/about_astral'):
		send_message.build_message(bot, from_id, ('about_astral'))
		return

	elif query_data == ('/about_ono'):
		send_message.build_message(bot, from_id, ('about_ono'))
		return

	elif query_data == ('/about_beelzebub'):
		send_message.build_message(bot, from_id, ('about_beelzebub'))
		return

	elif query_data == ('/about_child_of_darkness'):
		send_message.build_message(bot, from_id, ('about_child_of_darkness'))
		return

	elif query_data == ('/about_capernaum'):
		send_message.build_message(bot, from_id, ('about_capernaum'))
		return

	elif query_data == ('/about_sin'):
		send_message.build_message(bot, from_id, ('about_sin'))
		return

	elif query_data == ('/about_babylon'):
		send_message.build_message(bot, from_id, ('about_babylon'))
		return

	elif query_data == ('/about_folks'):
		send_message.build_message(bot, from_id, ('about_folks'))
		return

	elif query_data == ('/about_gl'):
		send_message.build_message(bot, from_id, ('about_gl'))
		return

	elif query_data == ('/about_thiefhunt'):
		send_message.build_message(bot, from_id, ('about_thiefhunt'))
		return

	elif query_data == ('/about_tfd'):
		send_message.build_message(bot, from_id, ('about_tfd'))
		return

	elif query_data == ('/about_passanger'):
		send_message.build_message(bot, from_id, ('about_passanger'))
		return

	elif query_data == ('/about_slave'):
		send_message.build_message(bot, from_id, ('about_slave'))
		return

	elif query_data == ('/about_gb'):
		send_message.build_message(bot, from_id, ('about_gb'))
		return

	elif query_data == ('/about_masterpiece'):
		send_message.build_message(bot, from_id, ('about_masterpiece'))
		return

	elif query_data == ('/about_shazam'):
		send_message.build_message(bot, from_id, ('about_shazam'))
		return

''' Метод для подгрузки новых сообщений '''
MessageLoop(bot, {'chat': handle, 
	'callback_query': callback_response}).run_as_thread()

print("Ready !")

''' Делает код бесконечным '''
while True:
	time.sleep(1)

'''
Что-то не понятно?
Пиши мне:
Telegram > @sorry_but_i_amoral
Vk > vk.com/sorry_but_i_amoral 
'''