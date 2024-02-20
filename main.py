import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from config_data.config import Config, load_config

# Включение логирования, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Загрузка конфигурации в переменную config
config: Config = load_config()

# Создание объектов бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Hello!')


# Хэндлер на команду /test1
@dp.message(Command('test1'))
async def cmd_test1(message: Message):
    await message.answer('Test 1')


# Пример без декоратора, с регистрацией в диспетчере
# Хэндлер на команду /test2
async def cmd_test2(message: Message):
    await message.answer('Test 2')
# Где-то в другом месте, например, в функции main():
# Регистрация хэндлера в диспетчере
dp.message.register(cmd_test2, Command('test2'))


# Хэндлер для отправки сообщения в другой чат
@dp.message(Command('dice'))
async def cmd_dice(message: Message):
    await bot.send_dice(-100123456789, emoji=DiceEmoji.DICE)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
