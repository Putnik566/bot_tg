from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text, italic, bold
from aiogram.types import ParseMode
import emoji

TOKEN = '5081083524:AAHgLEg2SCzabY8-H8dp5A9rMi8MEsio4D8'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    msg = text(italic(emoji.emojize(':vampire:') + "Hi! Welcome kvest_BOT !!!" + emoji.emojize(':vampire:')))
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg1 = text(bold(emoji.emojize(':fox:') + "command" + emoji.emojize(':fox:')))
    await message.reply(msg1, parse_mode=ParseMode.MARKDOWN)


if __name__ == "__main__":
    executor.start_polling(dp)

