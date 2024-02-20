import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from config_data.config import Config, load_config

# Включение логирования, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Загрузка конфигурации в переменную config
config: Config = load_config()

# Создание объектов бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

@dp.message(Command('add_to_list'))
async def cmd_add_to_list(message: Message, mylist: list[int]):
    mylist.append(7)
    await message.answer('Добавлено число 7')

@dp.message(Command('show_list'))
async def cmd_show_list(message: Message, mylist: list[int]):
    await message.answer(f'Ваш список: {mylist}')

@dp.message(Command('info'))
async def cmd_info(message: Message, started_at: str):
    await message.answer(f'Бот запущен {started_at}')

# Запуск процесса поллинга новых апдейтов
async def main():
    dp['started_at'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == '__main__':
    asyncio.run(main())
