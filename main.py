import asyncio  # Импорт асинхронного ввода/вывода
import configs.config  # Импорт файла конфигурации, где обычно хранится токен бота
from aiogram import Bot, Dispatcher  # Импорт основных классов из aiogram
import logging  # Импорт модуля логирования
from handlers import common, career_choice, msg


async def main():  # Главная асинхронная функция
    logging.basicConfig(level=logging.INFO)  # Настройка логирования для отображения информационных сообщений
    bot = Bot(token=configs.config.token)  # Создаем экземпляр бота с токеном из файла configs
    dp = Dispatcher()  # Создаем экземпляр диспетчера

    dp.include_router(common.router)
    dp.include_router(career_choice.router)
    dp.include_router(msg.router)

    await dp.start_polling(bot)  # Запуск бота на опрос сообщений


if __name__ == '__main__':  # Если файл запущен как основной, а не импортирован
    asyncio.run(main())  # Запускаем асинхронный цикл
