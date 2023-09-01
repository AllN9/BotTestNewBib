import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class ClientState(StatesGroup):
	'''Хранит на каком этапе диалога находится клиент'''
	NONE_STATE = State()
	TEAM_STATE = State()
	LEADER_STATE = State()
	DOIT_STATE = State()
	DETR_STATE = State()
	MEAN_STATE = State()
	ENERGY_STATE = State()

bot = Bot(token=config.TOKEN)

# storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='my_fsm_key')
# storage = MongoStorage(host='localhost', port=27017, db_name='aiogram_fsm')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message, state: FSMContext) -> None:
    sti = open('static/welcome.webp', 'rb')
    await bot.send_sticker(message.chat.id, sti)

    await bot.send_message(message.chat.id, "На связи Региональная команда твой ход. Это бот Лёха.\nОн очень добрый.".format(message.from_user, bot.get_me()), parse_mode='html')
    await bot.send_message(message.chat.id, "Сегодня он проведет вам квест! Пишите сюда слова с коробок и получайте задания.".format(message.from_user, bot.get_me()), parse_mode='html')
    await state.set_state(ClientState.NONE_STATE)

@dp.message_handler(state=ClientState.NONE_STATE, content_types=['text'])
async def Task(message: types.Message, state: FSMContext):
	if((message.text == "Команда") or (message.text == "команда")):
		await bot.send_message(message.chat.id, "_\"Человек – существо социальное\"_ - так говорили нам на уроках обществознания. А мы и не спорим!\n\n*Задание:*\n\nСфотографируетесь всей командой _(группой)_ и пришли фото сюда в чат. Мы сделаем целый коллаж фото, и поделимся у себя в группе.\nЗаходи и смотри: [ссылка](https://vk.com/tvoyhod33)".format(message.from_user, bot.get_me()), parse_mode='Markdown')
		await state.set_state(ClientState.TEAM_STATE)
	elif(message.text == "Определяю" or message.text == "определяю"):
		await bot.send_message(message.chat.id, "Региональная команда помогает проекту [\"Конструктив\"](https://vk.com/konstruktiv_official).\nРебята занимаются популяризацией инженерного образования в интересной форме. Сейчас они проводят розыгрыш, [участвуй](https://vk.com/wall-221131579_44).\nМы можем больше, когда мы вместе!\n\n*Задание:*\n\nЧто не хватает молодёжи в нашем регионе? _Напиши свои идеи и отправьте ответным сообщение_. А мы с Молодёжным советом подумаем над их реализацией!".format(message.from_user, bot.get_me()), parse_mode='Markdown')
		await state.set_state(ClientState.DETR_STATE)
	elif(message.text == "Энергия" or message.text == "энергия"):
		await bot.send_message(message.chat.id, "Совсем не обязательно говорить с человеком о литературе, иногда достаточно просто танцевать с ним. А вы как думаете?\n\n*Задание:*\n\nСними видео-танец, как в [примере](https://drive.google.com/file/d/1N49aQ8zEm_9Y8YylONO21IuGeCNkFSrS/view?usp=drive_link).** Отправь видео** со своей командой ответным письмом. А мы позже соберём видео и выложим у нас в соц сетях: [ссылка](https://vk.com/tvoyhod33)".format(message.from_user, bot.get_me()), parse_mode='Markdown')
		await state.set_state(ClientState.ENERGY_STATE)
	elif(message.text == "Лидер" or message.text == "лидер"):
		await bot.send_message(message.chat.id, "Лидерам не хватает любви, а любви не хватает лидеров.\n\n*Задание:*\n\nСделай фото с региональным координатором Твой Ход. _Разузнать кто это из ребят на площадке тебе предстоит самому_.\nСкорей знакомься с командой и делай фото, присылай его ответным письмом!".format(message.from_user, bot.get_me()), parse_mode='Markdown')
		await state.set_state(ClientState.LEADER_STATE)
	elif(message.text == "Смысл" or message.text == "смысл"):
		await bot.send_message(message.chat.id, "В ожидании чуда делай добрые дела. Тогда и чудо придет к тебе не с пустыми руками. Такой принцип у нашей команды. Как вы думаете как звучит смысл проекта Твой Ход?\n\n*Задание:*\n\nРасшифруйте фразу с Азбуки Морзе и присылай в чат, ответным письмом.".format(message.from_user, bot.get_me()), parse_mode='Markdown')
		task = open('static/task.jpg', 'rb')
		await bot.send_photo(message.chat.id, task)
		ABC = open('static/ABC.jpg', 'rb')
		await bot.send_photo(message.chat.id, ABC)
		await state.set_state(ClientState.MEAN_STATE)
	elif(message.text == "Делаю" or message.text == "делаю"):
		await bot.send_message(message.chat.id, "Наша команда помогает проекту [\"Полюби жизнь заново\"](http://lovelifeanew.tk.tilda.ws/). Ребята занимаются созданием компетентной команды волонтеров, чтобы организовывать досуг для детей, посещающих реабилитационные центры и находящихся на стационарном лечении.\n\n*Задание:*\n\nНарисуте мини открытку для детей. А команда волонтёров подарит их ребятам. Не забудьте сфотографировать её и загрузить фото в чат.".format(message.from_user, bot.get_me()), parse_mode='Markdown')
		await state.set_state(ClientState.DOIT_STATE)


@dp.message_handler(state=ClientState.TEAM_STATE, content_types=['text']) 
async def handle_photoTEAM(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Не обманывай меня, это не фото!".format(message.from_user, bot.get_me()), parse_mode='Markdown')

@dp.message_handler(state=ClientState.DETR_STATE, content_types=['text']) 
async def handle_photoDETR(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Хм, хорошие мысли.\n\nПиши следующее слово.".format(message.from_user, bot.get_me()), parse_mode='Markdown')
    await state.set_state(ClientState.NONE_STATE)

@dp.message_handler(state=ClientState.LEADER_STATE, content_types=['text']) 
async def handle_photoLEADER(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Вы жадины? поделитесь со мной фото!".format(message.from_user, bot.get_me()), parse_mode='Markdown')

@dp.message_handler(state=ClientState.DOIT_STATE, content_types=['text']) 
async def handle_photoDOIT(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Мне нужно фото открытки, хочу вспоминать вас холодными вечерами.".format(message.from_user, bot.get_me()), parse_mode='Markdown')

@dp.message_handler(state=ClientState.MEAN_STATE, content_types=['text']) 
async def handle_photoMEAN(message: types.Message, state: FSMContext):
    if(message.text == "Живу и создаю в России" or message.text == "живу и создаю в России" or message.text == "Живу и создаю в россии" or message.text == "живу и создаю в россии"):
        await bot.send_message(message.chat.id, "Верно, мы можем больше когда мы вместе!\n\nПиши следующее слово.".format(message.from_user, bot.get_me()), parse_mode='Markdown')
        await state.set_state(ClientState.NONE_STATE)
    else:
        await bot.send_message(message.chat.id, "Попробуйте вновь, у вас получиться!".format(message.from_user, bot.get_me()), parse_mode='Markdown')

@dp.message_handler(state=ClientState.ENERGY_STATE, content_types=['text']) 
async def handle_photoENERGY(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Это разве видео? я умный бот и рабираюсь в этом.".format(message.from_user, bot.get_me()), parse_mode='Markdown')

@dp.message_handler(state=ClientState.TEAM_STATE, content_types=['photo']) 
async def handle_photoTEAM(message: types.Message, state: FSMContext):
	# Получаем информацию о фото 
    await state.update_data(CITY=True)
    username = message.from_user.username 
    photo_info = message.photo[-1] 
    file_id = photo_info.file_id
    # Скачиваем фото 
    file_info = await bot.get_file(file_id) 
    file_url = f"https://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}"
    await bot.send_message(885468895, file_url)
    await message.answer("Прекрасное фото, каждому бы такую команду.\n\nПиши следующее слово.")

    await state.set_state(ClientState.NONE_STATE)
	
@dp.message_handler(state=ClientState.LEADER_STATE, content_types=['photo']) 
async def handle_photoLEADER(message: types.Message, state: FSMContext):
	# Получаем информацию о фото 
    await state.update_data(CITY=True)
    username = message.from_user.username 
    photo_info = message.photo[-1] 
    file_id = photo_info.file_id
    # Скачиваем фото 
    file_info = await bot.get_file(file_id) 
    file_url = f"https://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}"
    await bot.send_message(885468895, file_url)
    await message.answer("Правда милашка?\n\nПиши следующее слово.")

    await state.set_state(ClientState.NONE_STATE)

@dp.message_handler(state=ClientState.DOIT_STATE, content_types=['photo']) 
async def handle_photoDOIT(message: types.Message, state: FSMContext):
	# Получаем информацию о фото 
    await state.update_data(CITY=True)
    username = message.from_user.username 
    photo_info = message.photo[-1] 
    file_id = photo_info.file_id
    # Скачиваем фото 
    file_info = await bot.get_file(file_id) 
    file_url = f"https://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}"
    await bot.send_message(885468895, file_url)
    await message.answer("Полюби жизнь заново - три главных слова.\n\nПиши следующее слово.")

    await state.set_state(ClientState.NONE_STATE)

@dp.message_handler(state=ClientState.ENERGY_STATE, content_types=['video']) 
async def handle_photoENERGY(message: types.Message, state: FSMContext):
    userID= message.chat.id 
    username = message.from_user.username 
    print(f'{message.video=}') 
	#for document in message.document: 
    file_info = await bot.get_file(message.video.file_id) 
    print(file_info)
    file_url = f"https://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}"
    await bot.send_message(885468895, "{0.first_name} прислал вам документ".format(message.from_user, bot.get_me()), parse_mode='Markdown')
    await bot.send_message(885468895, file_url)
    await bot.send_message(message.chat.id, "И звание самых крутых танцоров, присуждаеться вашей команде!\n\nПиши следующее слово.")

    await state.set_state(ClientState.NONE_STATE)

@dp.message_handler(state=ClientState.ENERGY_STATE, content_types=['document']) 
async def handle_photoENERGY(message: types.Message, state: FSMContext):
    await state.update_data(CITY=True)
    userID= message.chat.id 
    username = message.from_user.username
    print(f'{message.document=}') 
	#for document in message.document:
    file_info = await bot.get_file(message.document.file_id) 
    print(file_info)
    file_url = f"https://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}"
    await bot.send_message(885468895, "{0.first_name} прислал вам документ".format(message.from_user, bot.get_me()), parse_mode='Markdown')
    await bot.send_message(885468895, file_url) 
    # Отправляем ответное сообщение
    await bot.send_message(message.chat.id, "И звание самых крутых танцоров, присуждаеться вашей команде!\n\nПиши следующее слово.")

    await state.set_state(ClientState.NONE_STATE)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)