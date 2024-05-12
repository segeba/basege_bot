# Импорт асинхронного ввода/вывода
import asyncio
# Импорт файла конфигурации, где обычно хранится токен бота
import config
# Импорт основных классов из aiogram
from aiogram import Bot, Dispatcher, types, F
# Импорт фильтра команд из aiogram
from aiogram.filters.command import Command
# Импорт модуля логирования
import logging
# Импорт модуля random для генерации случайных чисел
import random
# Импорт клавиатуры KeyboardStart из файла keyboards.py
from keyboars.keyboards import keyword

# Настройка логирования для отображения информационных сообщений
logging.basicConfig(level=logging.INFO)
# Создаем экземпляр бота с токеном из файла config
bot = Bot(token=config.token)
# Создаем экземпляр диспетчера
dp = Dispatcher()

# Декоратор для обработки команды /start
@dp.message(Command(commands=['start']))
# Асинхронная функция для реакции на команду /start
async def start(message: types.Message):
    # Отправляем приветственное сообщение
    await message.answer(f'Привет, {message.from_user.full_name}! \n Список команд: \n /user - имя пользователя \n /rand - случайное число', reply_markup=keyword)

@dp.message(F.text.lower() =='rand')
# перечисление команд списком через запетую - ['info', 'инфо']
@dp.message(Command(commands=['rand', 'рандом']))
async def rand(message: types.Message):
    number = random.randint(0,100)
    await message.answer(f'Случайное число - {number}')

@dp.message(Command(commands=['user']))
async def user(msg: types.Message):
    print(msg.from_user.full_name)
    await msg.answer(f'Пользователь, {msg.chat.username}!')

@dp.message(Command(commands=['стоп'])) # Для нескольких команд один набор действий
@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Пока, {message.chat.first_name}!')

# поиск различного текста в сообщении от пользователя (например, нецензурные слова)
@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально. А у тебя как?')
    else:
        await message.reply('Моя твоя не понимать!')

# Главная асинхронная функция
async def main():
    # Запуск бота на опрос сообщений
    await dp.start_polling(bot)

# Если файл запущен как основной, а не импортирован
if __name__ == '__main__':
    # Запускаем асинхронный цикл
    asyncio.run(main())