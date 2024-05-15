from aiogram import Router, types, F
from aiogram.filters.command import Command
import random
from keyboars.keyboard import keyword
from utils.randomfox import fox


router = Router()


@router.message(Command(commands=['start']))
# Асинхронная функция для реакции на команду /start
async def start(message: types.Message):
    # Отправляем приветственное сообщение
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyword)
                         #f'\n Список команд: \n /user - имя пользователя \n /rand - случайное число',



@router.message(Command(commands=['rand', 'рандом']))
async def rand(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Случайное число - {number}')


@router.message(Command(commands=['user']))
async def user(msg: types.Message):
    print(msg.from_user.full_name)
    await msg.answer(f'Пользователь, {msg.chat.username}!')


# @dp.message(Command(commands=['стоп'])) # Для нескольких команд один набор действий
@router.message(Command(commands=['stop']))
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Пока, {message.chat.first_name}!')


@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису!')
    await message.answer_photo(img_fox)
    # img_fox = fox()
    # await bot.send_photo(message.from_user.id, img_fox)
