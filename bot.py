import random
import re
import json
import logging
import os
from telegram import Update, ForceReply, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '5081083524:AAHgLEg2SCzabY8-H8dp5A9rMi8MEsio4D8'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

change_time_pattern = r'^([Пп]оменяй |)время (\d{1,2}:\d{1,2}) (\d{1,2}:\d{1,2})'
change_time_and_day_pattern = r'^([Пп]оменяй) (\S+) (\d{1,2}:\d{1,2}) (\S+)'

change_time_pattern_error = r'(\S+) (\S+) (\S+)'
change_day_pattern_error = r'^([Пп]оменяй) (\S+)'

day_names_eng = {}
with open('rasp_eng.json', 'r', encoding='utf-8') as day_names_eng_file:
    day_names_eng = json.load(day_names_eng_file)
    #############################################################
raspisanie_data = {}
with open('raspisanie.json', 'r', encoding='utf-8') as rasp_file:
    raspisanie_data = json.load(rasp_file)


def save_rasp():
    global raspisanie_data, day_names_eng
    with open('raspisanie.json', 'w', encoding='utf-8') as rasp_file_d:
        json.dump(raspisanie_data, rasp_file_d, ensure_ascii=False)
    with open('rasp_eng.json', 'r', encoding='utf-8') as day_names_eng_file:
        day_names_eng = json.load(day_names_eng_file)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!', reply_markup=ForceReply(selective=True))
    update.message.reply_text('-', reply_markup=ReplyKeyboardMarkup(
        [
            ['/monday', '/thursday', '/wednesday'],
            ['/thursday', '/friday'],
        ],
        one_time_keyboard=True,
        resize_keyboard=True,
        input_field_placeholder='command:'))


def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        """command:
        /start
        /info
        /help
        /Monday-расписание на понедельник
        /Tuesday-расписание на вторник
        /Wednesday-расписание на среду
        /Thursday-расписание на четверг
        /Friday-расписание на пятницу
        Шаблоны:
        *Поменяй время - если вы хотите поменять время  в расписании. Пример:(Поменяй время 8:30)
        *Поменяй - если вы хотите поменять день, время и урок в расписании. Пример:(Поменяй понедельник 8:30 физика)
        """
    )


def info_commad(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
        command:
        /start
        /info
        /help
        /Monday-расписание на понедельник
        /Tuesday-расписание на вторник
        /Wednesday-расписание на среду
        /Thursday-расписание на четверг
        /Friday-расписание на пятницу
        Шаблоны:
        *Поменяй время - если вы хотите поменять время  в расписании. Пример:(Поменяй время 8:30)
        *Поменяй - если вы хотите поменять день, время и урок в расписании. Пример:(Поменяй понедельник 8:30 физика)
        """)


def greeting_a_new_user(update: Update, context: CallbackContext):
    user = update.chat_member
    user.update.message.reply_markdown_v2(fr'welcome{user.mention_markdown_v2()}\!!!',
                                          reply_markup=ForceReply(selective=True))


def raspisanie(update: Update, context: CallbackContext):
    output = re.findall(change_time_pattern_error, update.message.text)
    if len(output) != 0:
        update.message.reply_text("неправельный ввод")
        return

    key = update.message.text[1:] if update.message.text.startswith('/') else update.message.text
    for message in check_resp(key):
        update.message.reply_text(message)


def check_resp(message):
    messages = []

    key = message[0].upper() + message[1:].lower()
    eng_key = day_names_eng.get(key)

    if eng_key is not None:
        key = eng_key

    day_rasp = raspisanie_data.get(key)
    if day_rasp is None:
        messages.append("такого дня недели не существует")
        return messages

    messages.append("Hello!")
    messages.append("Your raspisanie")
    data = ""
    for time_lesson in day_rasp.keys():
        if time_lesson == "date": continue
        data += f'{time_lesson}-{day_rasp[time_lesson]}\n'

    messages.append(f'Расписание на: {key}, ({day_rasp["date"]})')
    messages.append(data)
    return messages


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def foto(update, context: CallbackContext):
    reply_command = ["cool foto", "good foto", "beautiful photo", "nice foto"]
    update.message.reply_text(random.choice(reply_command))


def men_day(update: Update, context: CallbackContext):
    global raspisanie_data, day_names_eng

    text = update.message.text
    output = re.findall(change_time_and_day_pattern, text)
    if len(output) != 1:
        update.message.reply_text("не правильный ввод")
        return

    _, dayName, timeName, lessonName = output[0]

    lessonName = lessonName[0].upper() + lessonName[1:].lower()
    key = dayName[0].upper() + dayName[1:].lower()
    eng_key = day_names_eng.get(key)
    if eng_key is not None:
        key = eng_key

    day_rasp = raspisanie_data.get(key)
    if day_rasp is None:
        update.message.reply_text("такого дня недели не существует")
        return

    isChanged = False
    for timeRasp in raspisanie_data[key].keys():
        if timeName not in timeRasp: continue
        raspisanie_data[key][timeRasp] = lessonName
        isChanged = True
        break

    if isChanged is not isChanged:
        update.message.reply_text("такого времени не существует")
        return

    save_rasp()
    update.message.reply_text("Ok")


def men_time(update: Update, context: CallbackContext, encoding='utf-8'):
    global raspisanie_data
    text = update.message.text
    output = re.findall(change_time_pattern, text)

    if len(output) != 1:
        # TODO: send message to user about invalid message
        update.message.reply_text("такого времени не существует")
        return

    _, from_time, to_time = output[0]

    for day in dict(raspisanie_data).keys():
        for time_name in dict(raspisanie_data[day]).keys():
            if from_time in time_name:
                raspisanie_data[day][time_name.replace(from_time, to_time)] = raspisanie_data[day][time_name]
                del raspisanie_data[day][time_name]

    save_rasp()
    update.message.reply_text("Ok")


if __name__ == '__main__':
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("info", info_commad))
    dispatcher.add_handler(MessageHandler(Filters.regex("^([Пп]оменяй время)"), men_time))
    dispatcher.add_handler(MessageHandler(Filters.regex('^[Пп]оменяй'), men_day))
    dispatcher.add_handler(
        MessageHandler(Filters.text & (~Filters.regex("^поменяй время")) & (~Filters.regex('^поменяй')), raspisanie))

    dispatcher.add_handler(MessageHandler(Filters.photo, foto))
    # Start the Bot
    PORT=int(os.environ.get('PORT', '8443'))
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url="https://raspisanie-bot-101.herokuapp.com/" + TOKEN)
    updater.idle()
