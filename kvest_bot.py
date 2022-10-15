from aiogram import executor, Bot, types, Dispatcher
from aiogram.types import ParseMode, InputMediaPhoto, ContentType, Message
from aiogram.utils.markdown import text, italic, bold
import emoji
import json
Token = "5507190340:AAEv-n7CpB-GSxrQU2p2FE8hDDL1KT0FTKY"
bot = Bot(token=Token)
dp = Dispatcher(bot)

# 2) доделать функции( info_about_2_quest) """


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"{emoji.emojize(':fox:')}" + "Hi! Добро пожаловать в kvest_BOT" + f"{emoji.emojize(':fox:')}" + "\n"
                           f"{emoji.emojize(':fire:')}" + "Basic command:" + f"{emoji.emojize(':fire:')}" + "\n"
                           f"{emoji.emojize(':collision:')}" + "/start - Launching the bot" + f"{emoji.emojize(':collision:')}" + "\n"
                           f"{emoji.emojize(':collision:')}" + "/help - Output of bot commands info" + f"{emoji.emojize(':collision:')}" + "\n"
                           f"{emoji.emojize(':collision:')}" + "/info - Information about the bot and author" + f"{emoji.emojize(':collision:')}")


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):  # check mark button, joker
    await bot.send_message(message.from_user.id,
                           f"{emoji.emojize(':fire:')}" + "All command:" + f"{emoji.emojize(':fire:')}" + "\n"
                           f"{emoji.emojize(':axe:')}" + "/start - Launching the bot" + f"{emoji.emojize(':axe:')}" + "\n"
                           f"{emoji.emojize(':jack-o-lantern:')}" + "/help - Output of bot commands info" + f"{emoji.emojize(':jack-o-lantern:')}" + "\n"
                           f"{emoji.emojize(':axe:')}" + "/info - Information about the bot and author " + f"{emoji.emojize(':axe:')}" + "\n"
                           f"{emoji.emojize(':jack-o-lantern:')}" + "/code - The whole bot code " + f"{emoji.emojize(':jack-o-lantern:')}" + "\n"
                           f"{emoji.emojize(':axe:')}" + "/info_about_1_quest - Information about the first quest" + f"{emoji.emojize(':axe:')}" + "\n"
                           f"{emoji.emojize(':jack-o-lantern:')}" + "/info_about_2_quest - Information about the second quest" + f"{emoji.emojize(':jack-o-lantern:')}")


@dp.message_handler(commands=["info"])#Вывод информации о боте и авторе.
async def process_info_command(message: types.Message):
    msg = (f"{text(italic('Author:' ))}{text(bold(' Egor'))}\n"
           f"{text(italic('Age of the author: '))}{text(bold(' at the time of creation of the bot 17'))}\n"
           f"{text(italic('Author nickname:' ))}{text(bold(' @566'))}\n"
           f"{text(italic('Bot nick name for user: '))}{text(bold(' Kvest_BOT'))}\n"
           f"{text(italic('Author email: '))}{text(bold(' sasavaego05@gmail.com'))}\n"
           f"{text(italic('Bot nick name:'))}{text(bold(' Quest566_bot'))}\n"
           f"{text(italic('Status:'))}{text(bold(' in active development'))}\n"
           f"{text(italic('Creation idea: '))}{text(bold(' June 2022'))}\n"
           f"{text(italic('Realization: '))}{text(bold('beginning of August to i dont know'))}\n"
           f"{text(italic('Libraries used: '))}{text(bold(' i use aiogram, json, emoji, but I plan to also use Sqlalchemy, HTML and anything else if needed'))}\t \n"
           f"{text(italic('Goals: '))}{text(bold(' first'))}{text(italic(' to make a bot to the end'))}{text(bold(' second'))}{text(italic(' to study aiogram'))}{text(bold(' third'))}{text(italic(' to do lessons and project School'))}\n")
    await bot.send_message(message.from_user.id, msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['info_about_1_quest'])# Вывод информации о первом квесте.
async def process_Description_of_the_quest_1_comm(message: types.Message):
    await bot.send_message(message.from_user.id, "Информация о квесте:")
    with open('info_kvest.json', 'r', encoding="utf-8") as text_info_kvest_file:
        text_info_kvest = json.load(text_info_kvest_file)
        info = text_info_kvest['text_info']['info_1_kvest']
    await bot.send_message(message.from_user.id, info)

@dp.message_handler(commands=['info_about_2_quest'])# Вывод информации о втором квесте.
async def process_Description_of_the_quest_1_comm(message: types.Message):
    await bot.send_message(message.from_user.id, "Краткое содержание квеста:")
    with open('info_kvest.json', 'r', encoding="utf-8") as text_info_kvest_file:
        text_info_kvest = json.load(text_info_kvest_file)
        info = text_info_kvest['text_info']['info_2_kvest']
    await bot.send_message(message.from_user.id, info)
@dp.message_handler(commands=['code'])
async def process_code(message: Message): #Ответ для любопытных.
    await bot.send_sticker(message.from_user.id, sticker="https://s3.amazonaws.com/stickers.wiki/sziulife/1728403.160.webp",)
    await bot.send_message(message.from_user.id, "Извините, но кода здесь не будет!")


@dp.message_handler()
async def encho_process(msg: types.Message):
    await msg.reply(msg.from_user.id, msg.text)

#Ответ бота на не понятные ему сообщенияю.


@dp.message_handler(content_types=ContentType.ANY)
async def otclic_na_nezhdannyye_soobshcheniya(message: types.Message):
    msg = (f"{emoji.emojize(':ram:')} Дружище, я не знаю, что это.{emoji.emojize(':ram:')}\n"
           f"{emoji.emojize(':robot:')} Воспользуйтесь {text(bold('командой'))} /help {emoji.emojize(':robot:')}")
    await bot.send_message(message.from_user.id, msg, parse_mode=ParseMode.MARKDOWN,)


@dp.message_handler(content_types=ContentType.STICKER) # создаю обработчик, который выводит id STICKER, должен его ввводить, но увы нет.
async def photo_handler_proccess(message: Message):
    await message.reply(message.sticker[-1].file_id)

if __name__ == "__main__":
    executor.start_polling(dp)
