# Задача "Регистрация покупателей":

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from  aiogram.dispatcher import  FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить')
        ],
        [   KeyboardButton(text='Регистрация')
        ]
    ], resize_keyboard=True
)

kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calculate'),
        InlineKeyboardButton(text='Формулы расчёта', callback_data='shape')]
    ]
)

kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]
    ]
)

kb3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мужчина'),
            KeyboardButton(text='Женщина')
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()
    #(возраст, рост, вес, пол)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Я бот помогающий Вашему здоровью. \n выберите кнопку для продолжения', reply_markup=kb)

@dp.callback_query_handler(text=['calculate'])
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Ваш возраст:')
    await call.answer()
    await UserState.age.set()

@dp.callback_query_handler(text=['shape'])
async def get_formula(call: types.CallbackQuery):
    await call.message.answer('Формула расчёта Миффлина-Сан Жеора:\n'
                              '(10*вес + 6.25*рост + 5*возраст + 5) - для мужчин\n'
                              '(10*вес + 6.25*рост + 5*возраст - 161) - для женщин')
    await call.answer()
# карточки
@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    base = get_all_products()
    for number in base:
        await message.answer(f"Название: {number[1]} | Описание: {number[2]} | Цена: {number[3]}")
        with open(f'foto/{number[0]}.jpeg', 'rb') as file:
            await message.answer_photo(file)
    await message.answer(f'Выберите продукт для покупки.', reply_markup=kb2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb1)

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer("Бот поможет расcчитать суточный рацион в калориях\n"
                         "для Вашего возраста, роста, веса и пола", reply_markup=kb1)

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age_get = message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_get = message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async  def set_gender(message, state):
    await state.update_data(weight_get=message.text)
    await message.reply('Укажите свой пол Мужчина или Женщина):', reply_markup=kb3)
    await UserState.gender.set()

@dp.message_handler(state = UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender_get=message.text)
    data = await state.get_data()
    try:
        age = float(data['age_get'])
        weight = float(data['weight_get'])
        growth = float(data['growth_get'])
        gender = str(data['gender_get'])
    except:
        await  message.answer('Упс, что-то пошло не так, задано неверное значение.')
        await state.finish()

    if gender == 'Мужчина':
        calorie_intake_man = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.answer(f'Ваша норма в сутки для мужчин: {calorie_intake_man} ккал')
        await state.finish()
    else:
        calorie_intake_woman = 10 * weight + 6.25 * growth - 5 * age - 161
        await message.answer(f'Ваша норма в сутки для женщин: {calorie_intake_woman} ккал')
        await state.finish()

@dp.message_handler(text=['Регистрация'])
async def sihg_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит): ')
    # ожидание ввода имени в атрибут RegistrationState.username
    await RegistrationState.username.set()

# обработчик реагирует на состояние RegistrationState.username
@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    # условие проверки существования пользователя в таблице User БД
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        # запрашиваем новое состояние для RegistrationState.username
        await RegistrationState.username.set()
    else:
        # обновление данных в состоянии RegistrationState.username на message.text
        await state.update_data(username=message.text)
        # ожидание процедуры ввода email
        await message.answer("Введите свой email:")
        # ожидание ввода email в атрибут RegistrationState.email
        await RegistrationState.email.set()

# обработчик реагирует на состояние RegistrationState.email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    # обновление данных в состоянии RegistrationState.email на message.text
    await state.update_data(email=message.text)
    # ожидание процедуры ввода возраста
    await message.answer("Введите свой возраст:")
    # ожидание ввода возраста в атрибут RegistrationState.age
    await RegistrationState.age.set()

# обработчик реагирует на состояние RegistrationState.age
@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    # обновление данных в состоянии RegistrationState.age на message.text
    await state.update_data(age=message.text)
    user_data = await state.get_data()
    # запись в таблицу User БД собранные данные при помощи crud-функции add_user
    add_user(user_data['username'], user_data['email'], user_data['age'])
    await message.answer(f"{user_data['username']} зарегистрирован")
    # завершение приёма состояния при помощи метода finish()
    await state.finish()


@dp.message_handler(content_types=['text']) # commands=['start']
async def all_message(message: types.Message):
    await message.reply('Привет! Введите команду /start, чтобы начать общение.')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
