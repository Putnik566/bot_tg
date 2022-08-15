# 1) импортирование нужных модулей
from aiogram import Bot, Dispatcher, executor, types

# 2) получение токена от @BotFather.
Token = "5507190340:AAEv-n7CpB-GSxrQU2p2FE8hDDL1KT0FTKY"
# 3) Инициализация объектов бота и Dispatcher.
bot = Bot(token=Token)
dp = Dispatcher(bot)


# 4) Создание команду start.
@dp.message_handler(commands=["start"])
async def process_start_commands(message: types.Message):
    await message.reply("Hi!\n Добро пожаловать в kvest_BOT")


# 5) Создание команду help.
@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply("command: \n"
                        "/start\n" 
                        "/help\n"
                        "/quest_1\n"
                        "/quest_2\n"
                        "/Description_of_the_quest_№_1\n"
                        "/Description_of_the_quest_№_2\n")


# 6) Создание Обработчик сообщений.
@dp.message_handler()
async def echo_process(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


# 7)Чтобы получить сообщение от Telegram воспользуемся polling - это постоянный опрос сервера на наличие новый обновлений.
if __name__ == '__main__':
    executor.start_polling(dp)
