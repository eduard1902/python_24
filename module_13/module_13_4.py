from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from  aiogram.dispatcher import  FSMContext
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    #(возраст, рост, вес)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(text="Calories")
async def set_age(message):
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
async def send_calories(message, state):
    await state.update_data(weight_get=message.text)
    data = await state.get_data()
    try:
        age = float(data['age_get'])
        weight = float(data['weight_get'])
        growth = float(data['growth_get'])
    except:
        await  message.answer('Упс, что-то пошло не так, задано неверное значение.')
        await state.finish()

    # await message.answer(f' {data["age_get"]} ')
    # 1. Упрощенный вариант формулы Миффлина-Сан Жеора:
    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    # для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.ggggg

    calorie_intake_man = 10 * weight + 6.25 * growth - 5 * age + 5
    calorie_intake_woman = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Норма в сутки для мужчин: {calorie_intake_man} ккал')
    await message.answer(f'Норма в сутки для женщин: {calorie_intake_woman} ккал')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)