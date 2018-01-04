# -*- coding: utf-8 -*-
import os
import logging
import telegram
import random
from telegram.error import NetworkError, Unauthorized
from time import sleep
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
#!/usr/bin/env python
# -*- coding: utf-8 -*-

update_id = None
frases_env = os.environ['FRASES_TOKEN']
frases = frases_env.split(';')
keyword = os.environ['BOT_KEYWORD']
usernames_env = os.environ['USERNAMES']
usernames = usernames_env.split(';')

def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(token)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    global frases
    global keyword
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        pos = random.randint(0, len(frases)-1)
        rand = random.randint(0, 10)
        if update.message is not None and update.message.text is not None \
                and keyword in update.message.text.upper():
            text_up = update.message.text.lower()
            if rand == 5:
                if update.message.from_user.username == usernames[0]:
                    update.message.reply_text('loba apestosa ')
                if update.message.from_user.username == usernames[1]:
                    update.message.reply_text('puto lo que sos')
                if update.message.from_user.username == usernames[2]:
                    update.message.reply_text('claro que sí, Lady Lisnichuk')
                if update.message.from_user.username == usernames[3] and rand == 1:
                    update.message.reply_text('caraaancho')
            else:
                if ('menstruación' in text_up) or ('menstruacion' in text_up):
                    update.message.reply_text('FFFFFFFFFFFFFFFF')
                else:
                    update.message.reply_text(frases[pos])

if __name__ == '__main__':
    main()

