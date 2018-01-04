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
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""



update_id = None
frases = ['No puedo, tengo que salvar al mundo', 'cena en Paraguari?','Brenda buscame, tengo enfermo',
          'jajajaa gran turismo', 'sounds like a plan', 'nice try', 'honey dew', 'vos sos de verdad?',
          'costanera?', 'quieen le extraña al grupo random quien quien?', 'make sense', 'listo el pollo',
          'sure', 'suena bien', 'que rarojo', 'o tenes miedo?', 'loro guardian ataca de nuevo',
          'bueno mami', 'dont worry', 'dame comida']

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
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        pos = random.randint(0, len(frases)-1)
        rand = random.randint(0, 10)
        if update.message is not None and update.message.text is not None \
                and 'CARPINCHO' in update.message.text.upper():
            if rand == 5:
                if update.effective_user.username == 'BBQut':
                    update.message.reply_text('loba apestosa ')
                if update.effective_user.username == 'szalimben':
                    update.message.reply_text('puto lo que sos')
                if update.effective_user.username == 'YohaLisnichuk':
                    update.message.reply_text('claro que sí, Lady Lisnichuk')
                if update.effective_user.username == 'Daaaaaaaaaaaaaaaaaaaaaaaaaaaaani' and rand == 1:
                    update.message.reply_text('caraaancho')
            else:
                update.message.reply_text(frases[pos])

if __name__ == '__main__':
    main()

