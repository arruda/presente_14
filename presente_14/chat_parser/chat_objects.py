# -*- coding: utf-8 -*-

from __future__ import absolute_import


class ConversationGroup(object):
    date = ""
    conversations = []

    def __init__(self, conversations):
        super(ConversationGroup, self).__init__()
        self.conversations = conversations
        self.date = conversations[-1].date

    def __str__(self):
        return self.date + ': [%d]' % len(self.conversations)


class Conversation(object):
    date = ""
    msgs = []

    def __init__(self, date, msgs):
        super(Conversation, self).__init__()
        self.date = date
        self.msgs = msgs

    def __str__(self):
        return self.date + ': [%d]' % len(self.msgs)


class Message(object):
    author = ""
    msg = ""

    def __init__(self, author, msg):
        super(Message, self).__init__()
        self.author = author
        self.msg = msg

    def __str__(self):
        return self.author + ': ' + self.msg
