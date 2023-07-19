from aiogram import Bot,Dispatcher,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons
import states
import data
from aiogram.types import ReplyKeyboardRemove
from geopy.geocoders import Nominatim




bot=Bot('ТОКЕН')
dp=Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_cmd(message):
    start_txt=f'Здравствуйте, {message.from_user.first_name}\nВас приветствует информационный бот компании ООО "DOKOUTSOURCE"\nВыберите информацию, которую вы хотите получить!'
    user_id=message.from_user.id
    print(user_id)
    await message.answer(start_txt, reply_markup=buttons.inline_info())


@dp.callback_query_handler(text = 'btn1')
async def phone_number(message):
    await bot.send_message(message.from_user.id,text='+998990306443', reply_markup=buttons.inline_info())

@dp.callback_query_handler(text = 'btn2')
async def phone_number(message):
    await bot.send_location(message.from_user.id,latitude=41.303289, longitude=69.267604, reply_markup=buttons.inline_info())
    geolocator = Nominatim(user_agent="DOKOUTSOURCE")
    location = geolocator.reverse("41.303289, 69.267604")
    await bot.send_message(message.from_user.id, location)

#Создаем обработчик текстовых сообщений (всех основных кнопок)
# @dp.message_handler(content_types=['text'])
# async def text_process(message):
#     #Прописываем условия для кнопок главного меню
#     if message.text == 'Отправить резюме':
#         await message.answer('Отлично!\nСперва отправь свое имя', reply_markup=ReplyKeyboardRemove())
#         #Переход на этап получения ответа
#         await GetData.get_name.set()
#     elif message.text == 'Статус':
#         resume_id = 'BQACAgIAAxkBAAIDd2QzA9HJc_8woMJWH-_fmPJD18oFAAK0LQACYgKYSV4-UDvd-_jgLwQ'
#         # await message.answer_document(resume_id)
#         await message.answer_document(resume_id)
#         await message.answer('Ваше резюме еще не просмотренно! Ожидайте')
#
#     else:
#         await message.answer('Выберите кнопку', reply_markup=btns.main_menu())


executor.start_polling(dp)