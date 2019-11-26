# -*- coding: utf-8 -*-

import logging
import random
import time

from datetime import datetime


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(message)s')


def now():
    return datetime.utcnow()


class Client:
    name = None

    @staticmethod
    def push(user_id, msg):
        """ emulate sending message,
        do some random sleep, if exception does not occur finish task """

        logging.info('starting push: %s' % now())
        logging.info('msg: %s' % msg)

        time.sleep(random.randint(0, 6))
        assert random.choice((True, False))
        logging.info('ending push: %s' % now())

    def __repr__(self):
        return '%s' % self.name


class TelegramClient(Client):
    name = 'Telegram Client'


class WhatsAppClient(Client):
    name = 'WhatsApp Client'


class ViberClient(Client):
    name = 'Viber Client'
