from db import DataBase
from telegram.ext import MessageHandler, Filters, CommandHandler
from random import randint


def echo(update, context):
    db = DataBase()
    list_mess = db.get_val_collocations()
    db.__del__()
    len_list = len(list_mess)
    randint(0, len_list)
    massage = ''
    if isint(update.message.text):
        i = int(update.message.text)
    else:
        i = 3

    for elem in range(i):
        massage += list_mess[randint(0, len_list)][0] + ', '
    context.bot.send_message(chat_id=update.effective_chat.id, text=massage)


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def handle_start_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="отправляешь любое сообщение и получаешь три "
                                                                    "элемента. Если отправить число, то кол-во "
                                                                    "элементов будет состовлять числу")


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('help', handle_start_help))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    return dp