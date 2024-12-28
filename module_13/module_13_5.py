from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()
    #(возраст, рост, вес, пол)

kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
kb1 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
button = KeyboardButton('Рассчитать')
button1 = KeyboardButton('Информация')
button2 = KeyboardButton('Мужчина')
button3 = KeyboardButton('Женщина')
kb.row(button, button1)
kb1.row(button2, button3)
# kb.add(button)
# kb.add(button1)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Я бот помогающий Вашему здоровью. \n выберите кнопку для продолжения', reply_markup=kb)

@dp.message_handler(text="Рассчитать")
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

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
    await message.reply('Укажите свой пол Мужчина или Женщина):', reply_markup=kb1)
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

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer("Бот поможет рассчитать суточный рацион в калориях\n"
                         "для Вашего возраста, роста, веса и пола", reply_markup=kb)

@dp.message_handler(content_types=['text']) # commands=['start']
async def all_message(message: types.Message):
    await message.reply('Привет! Введите команду /start, чтобы начать общение.')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
