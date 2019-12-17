from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
#################
import os
import json
import jdatetime
import time
#################
TOKEN = "970337991:AAEbGl-vdFHxgi-YLaHQ0PiYAeBcrREhOOY"
updater = Updater(TOKEN , use_context=False)

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



PORT = int(os.environ.get('PORT', '8443'))
# updater.start_polling()
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://botpythonic.herokuapp.com/" + TOKEN)






