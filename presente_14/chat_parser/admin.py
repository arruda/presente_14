#-*- coding:utf-8 -*-
"""
    chat_parser.admin
    ~~~~~~~~~~~~~~

    chat_parser admin file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

from django.contrib import admin

from .models import ConversationGroupModel



admin.site.register(ConversationGroupModel, admin.ModelAdmin)
