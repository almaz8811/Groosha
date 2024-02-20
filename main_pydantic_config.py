import asyncio
import logging
from config_data.config_pydantic import config
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji

# Включение логирования, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Для записей с типом Secret* необходимо вызвать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '******'
# Создание объектов бота и диспетчера
bot: Bot = Bot(token=config.bot_token.get_secret_value())
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
