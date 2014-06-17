# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('chat_parser.views',
     url(r'^$', 'printing_chats', name='printing_chats'),

)
