from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
from glob import glob
from random import choice
from emoji import emojize
import settings

def fat(update, context):
    fats = glob('img/fat*.jpg')
    fat = choice(fats)

    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fat, 'rb'))


def echo(update, context):
    ustext=update.message.text
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    if ustext=="300":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Пожми руку трактористу")
    elif ustext=="жир":
        fats = glob('img/fat*.jpg')
        fat = choice(fats)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fat, 'rb'))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Go vzhopy")


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                 level=logging.INFO,filename="bot.log")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    logging.info(update.message.text)
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY, use_context=True)
    logging.info("Pojehali")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('fat', fat))

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    #fat_handler = MessageHandler(Filters.text & (~Filters.command), fat)
    #dp.add_handler(fat_handler)

    dp.add_handler(echo_handler)

    mybot.start_polling()
    mybot.idle()
main()
