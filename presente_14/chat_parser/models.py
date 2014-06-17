# -*- coding: utf-8 -*-
"""
    chat_parser.models
    ~~~~~~~~~~~~~~

    chat_parser models file

    :copyright: (c) 2014 by arruda.
"""

from __future__ import absolute_import

from django.db import models


class ConversationGroupModel(models.Model):
    """
    A grouping of conversations
    """
    date = models.DateTimeField(u'Date')

    class Meta:
        app_label = 'chat_parser'

    def __unicode__(self):
        return self.date


class ConversationModel(models.Model):
    """
    A group of messages
    """
    date = models.DateTimeField(u'Date')
    group = models.ForeignKey(ConversationGroupModel, related_name='conversations', blank=True, null=True)

    class Meta:
        app_label = 'chat_parser'

    def __unicode__(self):
        return self.date


class MessageModel(models.Model):
    """
    A message
    """

    author = models.CharField(u'Author', max_length=250)
    msg = models.TextField(u'Message')
    conversation = models.ForeignKey(ConversationModel, related_name='messages', blank=True, null=True)

    class Meta:
        app_label = 'chat_parser'

    def __unicode__(self):
        return self.author + ': ' + self.msg
