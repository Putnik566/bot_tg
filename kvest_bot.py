from aiogram import executor, Bot, types, Dispatcher
from aiogram.types import ParseMode, InputMediaPhoto
from aiogram.utils.markdown import text, italic, bold
import emoji

Token = "5507190340:AAEv-n7CpB-GSxrQU2p2FE8hDDL1KT0FTKY"
bot = Bot(token=Token)
dp = Dispatcher(bot)

# emoji
greating_emoji = "CAACAgIAAxkBAAEFkfFi-rsX0Oj165T_mM_gKb7hvyR0eQACigYAApb6EgWNCZXTii-gICkE"

kuplinov_stickers = ["CAACAgIAAxkBAAEFkkNi-s1T6HBdTWfQ_LiLTtLYn9E0QAACSQADLSW1IAqH30VMiLWTKQQ",
                     "CAACAgIAAxkBAAEFkkVi-s1asoewRnaO8Z7IdYADruwKAAN2AAMtJbUgvfgQllCtIFspBA",
                     "CAACAgIAAxkBAAEFkkdi-s1n36bQ8VmKhi2DyRx0aEnLMAACgAADLSW1IDLh24IwMIyDKQQ"]


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           emoji.emojize(':fox:') + "Hi! Добро пожаловать в kvest_BOT" + emoji.emojize(':fox:'))


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           emoji.emojize(':hundred points:') + f"command:{emoji.emojize(':hundred points:')}:\n"
                                                               "/start\n"
                                                               "/help\n"
                                                               "/Description_of_the_quest_№_1\n"
                                                               "/Description_of_the_quest_№_2\n")


@dp.message_handler(commands=['Description_of_the_quest_№_1'])
async def process_Description_of_the_quest_1_comm(message: types.Message):
    mess = text(italic("fdgkj kdfgjk kfg dfg "))
    await message.reply(mess, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler()
async def encho_process(msg: types.Message):
    await msg.reply(msg.from_user.id, msg.text)


if __name__ == "__main__":
    executor.start_polling(dp)
