# -*- coding: utf-8 -*-

from __future__ import absolute_import

import locale
import threading

from datetime import datetime
from contextlib import contextmanager

from .html_parser import parse_html, perc_done
from .models import ConversationGroupModel, ConversationModel, MessageModel

LOCALE_LOCK = threading.Lock()


@contextmanager
def setlocale(name):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)


def string_to_datetime(string):
    string = string.replace('Em: ', '').replace(' GMT-0300 (BRT)', '')
    date = None
    # Example to write a formatted English date
    with setlocale('C'):
        date = datetime.strptime(string, '%a %b %d %Y %H:%M:%S')

    return date


def gen_chat_models():
    from django.conf import settings

    print "parsing..."
    conversations_groups = parse_html(settings.EMAILS_PATH)

    total = len(conversations_groups)
    done = 0.0
    print "saving to DB..."
    for cg in conversations_groups:
        perc_done(done, total)
        date = string_to_datetime(cg.date)
        cg_model = ConversationGroupModel(date=date)
        cg_model.save()

        for conversation in cg.conversations:
            date = string_to_datetime(conversation.date)
            conversation_model = ConversationModel(date=date)
            cg_model.conversations.add(conversation_model)

            msgs_models = []
            last_author = ""
            for msg in conversation.msgs:
                same_author = True
                if last_author != msg.author:
                    last_author = msg.author
                    same_author = False
                if len(msgs_models) != 0:
                    #update last msg to the correct value
                    msgs_models[-1].is_next_same_author = same_author

                msg_model = MessageModel(
                    author=msg.author,
                    msg=msg.msg,
                    conversation=conversation_model
                )
                msgs_models.append(msg_model)
            MessageModel.objects.bulk_create(msgs_models)

        done = done + 1

    perc_done(done, total)
