import json

from aiogram import executor, Bot, types, Dispatcher
from aiogram.types import ParseMode, InputMediaPhoto
from aiogram.utils.markdown import text, italic, bold
import emoji

Token = "5507190340:AAEv-n7CpB-GSxrQU2p2FE8hDDL1KT0FTKY"
bot = Bot(token=Token)
dp = Dispatcher(bot)

text_info_kvest = {}
with open('info_kvest.json', 'r', encoding="utf-8") as text_info_kvest_file:
    text_info_kvest = json.load(text_info_kvest_file)

# emoji
greating_emoji = "CAACAgIAAxkBAAEFkfFi-rsX0Oj165T_mM_gKb7hvyR0eQACigYAApb6EgWNCZXTii-gICkE"

kuplinov_stickers = ["CAACAgIAAxkBAAEFkkNi-s1T6HBdTWfQ_LiLTtLYn9E0QAACSQADLSW1IAqH30VMiLWTKQQ",
                     "CAACAgIAAxkBAAEFkkVi-s1asoewRnaO8Z7IdYADruwKAAN2AAMtJbUgvfgQllCtIFspBA",
                     "CAACAgIAAxkBAAEFkkdi-s1n36bQ8VmKhi2DyRx0aEnLMAACgAADLSW1IDLh24IwMIyDKQQ"]


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"{emoji.emojize(':fox:')}" + "Hi! Добро пожаловать в kvest_BOT" + f"{emoji.emojize(':fox:')}" + "\n"
                           f"{emoji.emojize(':fire:')}" + "command:" + f"{emoji.emojize(':fire:')}" + "\n"
                           f"{emoji.emojize(':collision:')}" + "/start" + f"{emoji.emojize(':collision:')}" + "\n"
                           f"{emoji.emojize(':collision:')}" + "/help" + f"{emoji.emojize(':collision:')}" + "\n"                                                  
                           f"{emoji.emojize(':collision:')}" + "/Description_of_the_quest_1" + f"{emoji.emojize(':collision:')}" + "\n"
                           f"{emoji.emojize(':collision:')}" + "/Description_of_the_quest_2" + f"{emoji.emojize(':collision:')}")


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):  # check mark button
    await bot.send_message(message.from_user.id,
                           f"{emoji.emojize(':fire:')}" + "command:" + f"{emoji.emojize(':fire:')}" + "\n"
                           f"{emoji.emojize(':joker:')}" + "/start" + f"{emoji.emojize(':joker:')}" + "\n"
                           f"{emoji.emojize(':jack-o-lantern:')}" + "/help" + f"{emoji.emojize(':jack-o-lantern:')}" + "\n"
                           f"{emoji.emojize(':joker:')}" + "/info" + f"{emoji.emojize(':joker:')}" + "\n"
                           f"{emoji.emojize(':jack-o-lantern:')}" + "/info_about_1_quest" + f"{emoji.emojize(':jack-o-lantern:')}" + "\n"
                           f"{emoji.emojize(':joker:')}" + "/info_about_2_quest" + f"{emoji.emojize(':joker:')}")


@dp.message_handler(commands=["info"])
async def process_info_command(message: types.Message):
    await message.reply("")


@dp.message_handler(commands=['info_about_1_quest'])
async def process_Description_of_the_quest_1_comm(message: types.Message):
    await message.reply("Краткое содержание квеста:")
    #with open('info_kvest.json', "r", encoding="utf-8") as text_info_kvest_file:
    #   json.dump(text_info_kvest, text_info_kvest_file)

@dp.message_handler(commands=['info_about_2_quest'])
async def process_Description_of_the_quest_1_comm(message: types.Message):
    await message.reply("Краткое содержание квеста:")


@dp.message_handler()
async def encho_process(msg: types.Message):
    await msg.reply(msg.from_user.id, msg.text)


if __name__ == "__main__":
    executor.start_polling(dp)
