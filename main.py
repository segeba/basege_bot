
import asyncio  # Импорт асинхронного ввода/вывода
import config  # Импорт файла конфигурации, где обычно хранится токен бота
from aiogram import Bot, Dispatcher, types  # Импорт основных классов из aiogram
from aiogram.filters.command import Command  # Импорт фильтра команд из aiogram
import logging  # Импорт модуля логирования
import random  # Импорт модуля random для генерации случайных чисел

logging.basicConfig(level=logging.INFO) # Настройка логирования для отображения информационных сообщений

# Создание бъекта бота и диспетчера для обработки сообщений
bot = Bot(token=config.token) # Создаем экземпляр бота с токеном из файла config
dp = Dispatcher() # Создаем экземпляр диспетчера

@dp.message(Command(commands=['start'])) # Декоратор для обработки команды /start
async def start(message: types.Message): # Асинхронная функция для реакции на команду /start
    await message.answer(f'Привет, {message.from_user.full_name}!') # Отправляем приветственное сообщение

@dp.message(Command(commands=['info']))
async def start(message: types.Message):
    print(message.from_user.full_name)
    # await message.answer(f'Привет, {message}!')
    await message.answer(f'Информация о, {message.chat.first_name} {message.chat.last_name}!')

@dp.message(Command(commands=['user']))
async def start(message: types.Message):
    print(message.from_user.full_name)
    # await message.answer(f'Привет, {message}!')
    await message.answer(f'Пользователь, {message.chat.username}!')

@dp.message(Command(commands=['msg']))
async def start(message: types.Message):
    print(message.from_user.full_name)
    # await message.answer(f'Привет, {message}!')
    await message.answer(f'Пока, {message}!')

@dp.message(Command(commands=['git']))
async def start(message: types.Message):
    print(message.from_user.full_name)
    # await message.answer(f'Привет, {message}!')
    await message.answer(f'Проверка работы GIT!')

@dp.message(Command(commands=['стоп'])) # Для нескольких команд один набор действий
@dp.message(Command(commands=['stop']))
async def start(message: types.Message):
    print(message.from_user.full_name)
    # await message.answer(f'Привет, {message}!')
    await message.answer(f'Пока, {message.chat.first_name}!')

async def main(): # Главная асинхронная функция
    await dp.start_polling(bot) # Запуск бота на опрос сообщений

if __name__ == '__main__': # Если файл запущен как основной, а не импортирован
    asyncio.run(main()) # Запускаем асинхронный цикл