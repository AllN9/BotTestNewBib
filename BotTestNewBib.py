import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class ClientState(StatesGroup):
    '''Хранит на каком этапе диалога находится клиент'''
    START_ORDER = State()
    CITY_SELECTED = State()
    RESTAURANT_SELECTED = State()
    DISH_SELECTED = State()
    DRINK_SELECTED = State()
    PROCCESS_ORDER = State()
    NONE_STATE = State()
    TEAM_STATE = State()

bot = Bot(token=config.TOKEN)

# storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='my_fsm_key')
# storage = MongoStorage(host='localhost', port=27017, db_name='aiogram_fsm')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) 

@dp.message_handler(commands=['Go'])
async def start_proccess(message: types.Message, state: FSMContext) -> None:
    msg = '''Привет! 👋🤖 Я бот доставки еды! В каком ты городе?'''
    
    msk_btn = KeyboardButton('Москва')
    spb_btn = KeyboardButton('СПБ')
    voronezh_btn = KeyboardButton('Воронеж')
    lipetsk_btn = KeyboardButton('Липецк')
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(msk_btn, spb_btn) 
    markup.row(voronezh_btn, lipetsk_btn) 
            
    await message.answer(msg, reply_markup=markup)
    await state.set_state(ClientState.START_ORDER)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message, state: FSMContext) -> None:
    sti = open('static/welcome.webp', 'rb')
    await bot.send_sticker(message.chat.id, sti)

    await bot.send_message(message.chat.id, "На связи Региональная команда твой ход. Это бот Лёха.\nОн очень добрый.".format(message.from_user, bot.get_me()), parse_mode='html')
    await bot.send_message(message.chat.id, "Сегодня он проведет вам квест! Пишите сюда слова с коробок и получайте задания.".format(message.from_user, bot.get_me()), parse_mode='html')
    await state.set_state(ClientState.NONE_STATE)

@dp.message_handler(content_types=['text'])
async def Task(message):
	if((message.text == "Команда") or (message.text == "команда")):
		await bot.send_message(message.chat.id, "_\"Человек – существо социальное\"_ - так говорили нам на уроках обществознания. А мы и не спорим!\n\n*Задание:*\n\nСфотографируетесь всей командой _(группой)_ и пришли фото сюда в чат. Мы сделаем целый коллаж фото, и поделимся у себя в группе.\nЗаходи и смотри: [ссылка](https://vk.com/tvoyhod33)".format(message.from_user, bot.get_me()), parse_mode='Markdown')
	elif(message.text == "Определяю" or message.text == "определяю"):
		await bot.send_message(message.chat.id, "Региональная команда помогает проекту [\"Конструктив\"](https://vk.com/konstruktiv_official).\nРебята занимаются популяризацией инженерного образования в интересной форме. Сейчас они проводят розыгрыш, [участвуй](https://vk.com/wall-221131579_44).\nМы можем больше, когда мы вместе!\n\n*Задание:*\n\nЧто не хватает молодёжи в нашем регионе? _Напиши свои идеи и отправьте ответным сообщение_. А мы с Молодёжным советом подумаем над их реализацией!".format(message.from_user, bot.get_me()), parse_mode='Markdown')
	elif(message.text == "Энергия" or message.text == "энергия"):
		await bot.send_message(message.chat.id, "Совсем не обязательно говорить с человеком о литературе, иногда достаточно просто танцевать с ним. А вы как думаете?\n\n*Задание:*\n\nСними видео-танец, как в [примере](https://drive.google.com/file/d/1N49aQ8zEm_9Y8YylONO21IuGeCNkFSrS/view?usp=drive_link).** Отправь видео** со своей командой ответным письмом. А мы позже соберём видео и выложим у нас в соц сетях: [ссылка](https://vk.com/tvoyhod33)".format(message.from_user, bot.get_me()), parse_mode='Markdown')
	elif(message.text == "Лидер" or message.text == "лидер"):
		await bot.send_message(message.chat.id, "Лидерам не хватает любви, а любви не хватает лидеров.\n\n*Задание:*\n\nСделай фото с региональным координатором Твой Ход. _Разузнать кто это из ребят на площадке тебе предстоит самому_.\nСкорей знакомься с командой и делай фото, присылай его ответным письмом!".format(message.from_user, bot.get_me()), parse_mode='Markdown')
	elif(message.text == "Смысл" or message.text == "смысл"):
		await bot.send_message(message.chat.id, "В ожидании чуда делай добрые дела. Тогда и чудо придет к тебе не с пустыми руками. Такой принцип у нашей команды. Как вы думаете как звучит смысл проекта Твой Ход?\n\n*Задание:*\n\nРасшифруйте фразу с Азбуки Морзе и присылай в чат, ответным письмом.".format(message.from_user, bot.get_me()), parse_mode='Markdown')
		task = open('static/task.jpg', 'rb')
		await bot.send_photo(message.chat.id, task)
		ABC = open('static/ABC.jpg', 'rb')
		await bot.send_photo(message.chat.id, ABC)
	elif(message.text == "Делаю" or message.text == "делаю"):
		await bot.send_message(message.chat.id, "Наша команда помогает проекту [\"Полюби жизнь заново\"](http://lovelifeanew.tk.tilda.ws/). Ребята занимаются созданием компетентной команды волонтеров, чтобы организовывать досуг для детей, посещающих реабилитационные центры и находящихся на стационарном лечении.\n\n*Задание:*\n\nНарисуте мини открытку для детей. А команда волонтёров подарит их ребятам. Не забудьте сфотографировать её и загрузить фото в чат.".format(message.from_user, bot.get_me()), parse_mode='Markdown')
	elif(message.text == "Живу и создаю в России" or message.text == "живу и создаю в России" or message.text == "Живу и создаю в россии" or message.text == "живу и создаю в россии"):
		await bot.send_message(message.chat.id, "Верно, мы можем больше когда мы вместе!".format(message.from_user, bot.get_me()), parse_mode='Markdown')

@dp.message_handler(state=ClientState.NONE_STATE, content_types=['photo']) 
async def handle_photo(message: types.Message, state: FSMContext):
	# Получаем информацию о фото
    await state.update_data(CITY=True)
    username = message.from_user.username 
    photo_info = message.photo[-1] 
    file_id = photo_info.file_id
	# Скачиваем фото
    file_info = await bot.get_file(file_id) 
    file_url = f"https://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}"
    await bot.send_message(885468895, 'Hello 1!' + file_url)
    await message.answer("Прекрасное фото, продолжайте в том же духе!")
    
    await state.set_state(ClientState.TEAM_STATE)

@dp.message_handler(state=ClientState.TEAM_STATE, content_types=['photo']) 
async def handle_photo(message: types.Message, state: FSMContext):
	# Получаем информацию о фото 
    await state.update_data(CITY=True)
    username = message.from_user.username 
    photo_info = message.photo[-1] 
    file_id = photo_info.file_id
    # Скачиваем фото 
    file_info = await bot.get_file(file_id) 
    file_url = f"https://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}"
    await bot.send_message(885468895, 'Hello 2!' + file_url)
    await message.answer("Прекрасное фото, продолжайте в том же духе!")

    await state.set_state(ClientState.NONE_STATE)
     
@dp.message_handler(state=ClientState.START_ORDER)
async def choose_restoraunts_process(message: types.Message, state: FSMContext):
    user_msg = message.text
    await state.update_data(CITY=user_msg)
    
    dragon_rest_btn = KeyboardButton('Китайский дракон')
    pylounge_rest_btn = KeyboardButton('PyLounge')
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(dragon_rest_btn, pylounge_rest_btn) 
            
    await message.answer('Выберите заведение', reply_markup=markup)
    await state.set_state(ClientState.CITY_SELECTED) 


@dp.message_handler(state=ClientState.CITY_SELECTED)
async def dish_process(message: types.Message, state: FSMContext):
    user_msg = message.text
    await state.update_data(RESTAURANT=user_msg)
    
    soup_menu_btn = KeyboardButton('Суп')
    nosoup_menu_btn = KeyboardButton('Не суп')
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(soup_menu_btn, nosoup_menu_btn) 
            
    await message.answer('Выберите блюдо', reply_markup=markup)
    await state.set_state(ClientState.RESTAURANT_SELECTED) 


@dp.message_handler(state=ClientState.RESTAURANT_SELECTED)
async def drink_process(message: types.Message, state: FSMContext):
    user_msg = message.text
    await state.update_data(DISH=user_msg)
    
    cola_menu_btn = KeyboardButton('Кола')
    more_cool_cola_menu_btn = KeyboardButton('Тоже кола но РУССКАЯ!')
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(cola_menu_btn, more_cool_cola_menu_btn) 
            
    await message.answer('Выберите напиток', reply_markup=markup)
    await state.set_state(ClientState.DISH_SELECTED)
    
    
@dp.message_handler(state=ClientState.DISH_SELECTED)
async def order_process(message: types.Message, state: FSMContext):
    user_msg = message.text
    await state.update_data(DRINK=user_msg)
    
    proccess_btn = KeyboardButton('Оформить заказ')
    cancel_btn = KeyboardButton('Отмена')
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(proccess_btn, cancel_btn) 
            
    await message.answer('Мы почти закончили', reply_markup=markup)
    await state.set_state(ClientState.DRINK_SELECTED)      

@dp.message_handler(state=ClientState.DRINK_SELECTED)
async def finish_process(message: types.Message, state: FSMContext):
    user_msg = message.text
    if user_msg == 'Оформить заказ':
        user_state_data = await state.get_data()
        city = user_state_data['CITY']
        rest = user_state_data['RESTAURANT']
        dish = user_state_data['DISH']
        drink = user_state_data['DRINK']
        msg = f'''Ваш заказ: {dish} {drink} из {rest} ({city}) ОФОРМЛЕН!!!'''
        await message.answer(msg)
    else:
        await message.answer('Пока(')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)