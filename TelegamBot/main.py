from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as rd


bot = Bot(token='5620475208:AAF6Bl7aij6aBgCNSwfOxYpxtSXUbkXYuLk')
updater = Updater(token='5620475208:AAF6Bl7aij6aBgCNSwfOxYpxtSXUbkXYuLk')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Hello')


def rand(update, context):
    context.bot.send_message(update.effective_chat.id, f'{rd(1, 100)}')


def voice(update, context):
    text = update.message.text
    if 'прив' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'И тебе привет, мой дорогой друг!')
    else:
        context.bot.send_message(update.effective_chat.id, 'Я тебя не понимаю :(')


start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random', rand)
message_handler = MessageHandler(Filters.text, voice)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()  # ctrl + c


