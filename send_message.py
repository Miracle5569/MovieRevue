import telepot, os, time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


''' Метод для постройки сообщений '''
def build_message(bot, chat_id, msg_type):

	if msg_type == ('start'):

		message = ('''
🎬 Добро пожаловать на FreeMovie!

🎥 Здесь Вы можете найти и посмотреть фильм по жанрам!

🔍 На данный момент у нас в списке несколько жанров с подборкой фильмов к ним!
				
😃 Приятного использования!
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='К фильмам !', callback_data='/getMovies')],
			])

		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('getMovies'):

		message = ('''
🎞 Выберите жанр фильма для просмотра

📜 На данный момент доступны следущие жанры:
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Ужасы', callback_data='/horror'), InlineKeyboardButton(text='Драма', callback_data='/drama')],
			[InlineKeyboardButton(text='Экшен', callback_data='/action'), InlineKeyboardButton(text='Комедия', callback_data='/comedy')]
			])

		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('horror'):

		message = ('''
🎞 Выберите фильм/серию фильмов, чтобы посмотреть его

📜 Доступны фильмы:
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Серия фильмом "Астрал"', callback_data='/about_astral'), InlineKeyboardButton(text='Оно / Оно 2', callback_data='/about_ono')],
			[InlineKeyboardButton(text='Вельзевул', callback_data='/about_beelzebub'), InlineKeyboardButton(text='Дитя тьмы', callback_data='/about_child_of_darkness')],
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('drama'):

		message = ('''
🎞 Выберите фильм/серию фильмов, чтобы посмотреть его

📜 Доступны фильмы:
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Капернаум', callback_data='/about_capernaum'), InlineKeyboardButton(text='Грех', callback_data='/about_sin')],
			[InlineKeyboardButton(text='Вавилон', callback_data='/about_babylon'), InlineKeyboardButton(text='Близкие', callback_data='/about_folks')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('action'):

		message = ('''
🎞 Выберите фильм/серию фильмов, чтобы посмотреть

📜 Доступны фильмы:
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Великий уравнитель 2', callback_data='/about_gl'), InlineKeyboardButton(text='Охота на воров', callback_data='/about_thiefhunt')],
			[InlineKeyboardButton(text='Жажда смерти', callback_data='/about_tfd'), InlineKeyboardButton(text='Пассажир', callback_data='/about_passanger')],
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('comedy'):

		message = ('''
🎞 Выберите фильм/серию фильмов, чтобы посмотреть его

📜 Доступны фильмы:
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Холоп', callback_data='/about_slave'), InlineKeyboardButton(text='Зеленая книга', callback_data='/about_gb')],
			[InlineKeyboardButton(text='Шедевр', callback_data='/about_masterpiece'), InlineKeyboardButton(text='Шазам!', callback_data='/about_shazam')],
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_astral'):

		message = ('''
📌 «Астрал» — серия фильмов сценариста Ли Уоннелла, 
снимается с 2010 года. Серия фильмов выпущены 
компанией Blumhouse Productions и состоит из 4 
фильмов в жанрах ужасы, мистика и триллер, 
начиная с «Астрала» и на данный момент 
заканчивая «Астрал 4: Последний ключ».

👀 Посмотреть можно здесь:

1 часть:
http://f1.lordfilm7.tv/27084-astral-2010.html

2 часть:
http://f1.lordfilm7.tv/27085-astral-glava-2-2013.html

3 часть:
http://f1.lordfilm7.tv/27086-astral-3-2015.html

4 часть:
http://f1.lordfilm7.tv/27138-astral-4-posledniy-klyuch-2018.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_ono'):

		message = ('''
📌 «Оно» — американо-канадский фильм ужасов 1990 
года режиссёра Томми Ли Уоллеса, экранизация 
романа Стивена Кинга. Фильм состоит из 2 частей.
Первоначально «Оно» показали по телевидению, 
в утреннее время. Съёмки фильма проходили в 
период с 23 мая по 27 июля 1990 года.

👀 Посмотреть можно здесь:

1 часть:
https://hdrezka-ag.com/films/horror/24318-ono-2017.html

2 часть:
https://kinozabor.net/782-212-ono-2.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_beelzebub'):

		message = ('''
📌 Расследование серии шокирующих убийств 
приводит к священнику, отлученному от 
церкви за сатанинские ритуалы. Он и его 
приспешники стремятся приблизить 
апокалипсис, чтобы антихрист явился в 
человеческий мир и беспредельно властвовал. 
Главному герою придется выйти на тропу 
войны с настоящим злом.

👀 Посмотреть можно здесь:
https://kinokrad.co/336124-velzevul.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_child_of_darkness'):

		message = ('''
📌 «Дитя тьмы» — американский кинофильм, 
в жанре драма/психологический триллер 
режиссёра Жауме Кольет-Серра. Слоган фильма 
«There is something wrong with Esther». 
Премьера в США состоялась 24 июля 2009 года.

👀 Посмотреть можно здесь:
http://f1.lordfilm7.tv/34786-ditja-tmy-2009.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_capernaum'):

		message = ('''
📌 История юного Зейна — мальчика, живущего 
в бедной бейрутской семье. Несмотря на 
юный возраст, он ведёт себя как совершенно 
взрослый человек: работает, следит за 
младшими братьями и сёстрами, помогает 
своей любимой сестре справиться с месячными, 
мечтает учиться в школе и смотрит на мир с 
плохо скрываемой ненавистью.

👀 Посмотреть можно здесь:
http://f1.lordfilm7.tv/56135-kapernaum-2018.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_sin'):

		message = ('''
📌 Картина рассказывает об испытаниях на 
творческом пути гениального художника и 
скульптора Микеланджело Буонарроти, за 
преданность которого борются два самых 
могущественных семейства.

👀 Посмотреть можно здесь:
http://f1.lordfilm7.tv/59453-greh-2019.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_babylon'):

		message = ('''
📌 «Вавилон» — драматический кинофильм 2006 
года режиссёра Алехандро Гонсалеса 
Иньярриту. Обладатель многочисленных 
международных наград, номинант на 
премию «Оскар» как лучший фильм года.

👀 Посмотреть можно здесь:
http://f1.lordfilm7.tv/29990-vavilon-2006.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_folks'):

		message = ('''
📌 Москва, наши дни. В спальном районе в 
тесной небогатой квартире проживает 
семья из пяти человек. Каждый из них 
занят своим делом, у каждого из них 
багаж проблем, который мучает и требует 
выплеска. Каждый из них мечтает о 
поддержке и человеческом тепле, но не 
находит ни того, ни другого. Жизнь 
кажется совершенно невыносимой, и 
козлом отпущения становится беззащитная, 
проживающая в отдельной комнатке старуха.

👀 Посмотреть можно здесь:
https://www.kino-teatr.ru/kino/movie/ros/123286/online/
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_gl'):

		message = ('''
📌 «Великий уравнитель» — боевик режиссёра 
Антуана Фукуа по сценарию Ричарда Уэнка, 
основанный на одноимённом телесериале. 
В главной роли — Дензел Вашингтон, образ 
ключевого антагониста воплотил Мартон Чокаш. 
Премьера состоялась на кинофестивале в 
Торонто 7 сентября 2014 года. В США фильм 
вышел в широкий прокат 26 сентября 2014, 
в России — 25 сентября 2014

👀 Посмотреть можно здесь:

1 часть:
https://kinokrad.co/325601-2018-velikiy-uravnitel-2-2018.html

2 часть:
https://kinokrad.co/325601-2018-velikiy-uravnitel-2-2018.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_thiefhunt'):

		message = ('''
📌 «Охота на воров» — американский боевик 
режиссёра Кристиана Гьюдгэста. В главной
роли Джерард Батлер[2]. Премьера фильма 
в США состоялась 19 января 2018 года, в 
России — 8 февраля

👀 Посмотреть можно здесь:
https://hdrezka-ag.com/films/action/27263-ohota-na-vorov-2018.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_tfd'):

		message = ('''
📌 «Жажда смерти» — американский триллер 
Элая Рота. Ремейк одноимённого фильма 
Майкла Уиннера 1974 года[1]. Премьера 
в США состоялась 2 марта 2018 года

👀 Посмотреть можно здесь:
http://f1.lordfilm7.tv/27855-zhazhda-smerti-2018.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_passanger'):

		message = ('''
📌 «Пассажир» — американо-британский 
триллер 2018 года режиссёра Жауме 
Кольет-Серра о страховом агенте — 
бывшем полицейском, втянутом в 
преступный заговор, ставящий под 
угрозу его самого и близких ему людей.

👀 Посмотреть можно здесь:
http://f1.lordfilm7.tv/27251-passazhir-1.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_slave'):

		message = ('''
📌 Молодой мажор Гриша заигрался в 
красивую жизнь и решил, что ему 
всё дозволено. Он натворил много дел, 
и теперь ему грозит тюрьма. Чтобы 
исправить своего сына, отчаявшийся 
отец-олигарх идёт на крайние меры. 
Вместе со своим старинным другом-
психологом он придумывает уникальный 
проект: на базе заброшенной деревни 
воссоздаётся атмосфера России 
девятнадцатого века. Гриша попадает
в подстроенную аварию и якобы 
переносится в прошлое.

👀 Посмотреть можно здесь:
https://kinokrad.co/338987-holop.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_gb'):

		message = ('''
📌 «Зелёная книга» — американская 
биографическая комедийная драма 
режиссёра Питера Фаррелли, вышедшая 
на экраны в 2018 году. Картина 
рассказывает реальную историю 
путешествия по югу США известного 
джазового пианиста Дона Ширли и 
обычного водителя Тони Валлелонги, 
между которыми со временем возникает 
дружба. Главные роли исполнили 
Вигго Мортенсен, Махершала Али и 
Линда Карделлини.

👀 Посмотреть можно здесь:
https://kinokrad.co/331928-1-10-zeljonaya-knig.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_masterpiece'):

		message = ('''
📌 Хваткий арт-дилер из Буэнос-Айреса 
Артуро на протяжении многих лет 
сотрудничает с угрюмым и замкнутым 
художником-отшельником Ренцо. Несмотря 
на свой талант и преданность искусству, 
пожилой Ренцо переживает спад 
популярности. Для того чтобы повысить 
продажи его работ, Артуро придумывает 
рискованный план. Известно, что картины
возрастают в цене после смерти автора

👀 Посмотреть можно здесь:
http://f1.lordfilm7.tv/56116-shedevr-2018.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return

	elif msg_type == ('about_shazam'):

		message = ('''
📌 У парня появляется удивительная 
способность: в случае необходимости 
он может превращаться во взрослого
супергероя при помощи одного 
волшебного слова.

👀 Посмотреть можно здесь:
https://kinokrad.co/333607-shazam-2019.html
			''')

		keyboard = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Назад', callback_data='/getMovies')]
			])
		bot.sendMessage(chat_id, message, reply_markup = keyboard)
		return
