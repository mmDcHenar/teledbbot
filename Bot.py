# from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from logging import basicConfig, INFO, getLogger
from telegram.ext import Updater, CommandHandler, MessageHandler  # , Filters, InlineQueryHandler
from re import search
from threading import Thread
from queue import Queue
from redis import Redis
from time import time

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)

uid = Redis()
uname = Redis(db=1)

admins = [
    181781214,  # Me
    847482650,  # mmd(@sm0k7)
]


def is_admin(u):
    if u.message.chat_id in admins or u.message.from_user.id in admins:
        return True
    else:
        return False


def start(u, b):
    u.message.reply_text('Okay!\nI\'m here!\nSend me username or userid to search... ')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
    ef userid(u):
    msg = u.message.reply_text('Searching in database...')
    start = time()
    result = uid.get(u.message.text)
    end = time()
    msg.edit_text('🆔 UserID: '+u.message.text+'\n\n🔡 UserName: @'+result.decode().split(';')[1]+'\n\n🔢 Phone Number: +'+result.decode().split(';')[0]+''+ if result else '⚠️ UserID not found!')


def username(u):
    msg = u.message.reply_text('Searching in database...')
    start = time()
    result = uname.get(u.message.text.replace('@', ''))
    end = time()
    msg.edit_text('🆔 UserID: '+result.decode().split(';')[1]+'\n\n🔡 UserName: '+u.message.text.replace('@', '')+'\n\n🔢 Phone Number: +'+result.decode().split(';')[0] if result else '⚠️ UserName not found!')


def read(u, b):
    try:
        msg = int(u.message.text)
        userid(u)
    except:
        username(u)


def main():
    updater = Updater('1295745309:AAHyUIy_7UZnO532YfppPm9qcn06eqX-6zg', use_context=True)
    # job=updater.job_queue
    # job.run_once(online,0)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start, run_async=True))
    # dp.add_handler(CommandHandler('username', username, run_async=True))
    # dp.add_handler(CommandHandler('userid', userid, run_async=True))
    # dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_handler(MessageHandler(Filters.text, read, run_async=True))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
