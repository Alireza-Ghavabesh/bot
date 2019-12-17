from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
#################
import json
import jdatetime
import time
#################
from telegram import WebhookInfo
updater = Updater('970337991:AAEbGl-vdFHxgi-YLaHQ0PiYAeBcrREhOOY' , use_context=False)

def start(bot , update):
    JsonUpdate = update.to_dict()
    # x = json.dumps(JsonUpdate , indent = 4)
    # with open('update.json' , 'a+') as file:
    #     file.write("{}\n".format(x))
    # user_id = JsonUpdate['message']['from']['id'] # this option no was in doc
    user_id = update.message.from_user.id
    message_id = update.message.message_id
    chat_id = update.message.chat.id
    text = update.message.text
    if text == "time-fa":
        bot.send_message(chat_id, "your time-fa is : {}".format(str(jdatetime.datetime.now())))
    elif text == 'time-en':
        bot.send_message(chat_id , "your time-en is : {0}".format(str(time.ctime())))
    elif user_id != 213123:
        bot.send_message(chat_id, "this  [ {} ] is your user-id".format(json.dumps(user_id)))

start_command = MessageHandler(Filters.all , start)
updater.dispatcher.add_handler(start_command)

updater.start_polling()
updater.idle()





