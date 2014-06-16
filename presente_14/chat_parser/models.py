# -*- coding: utf-8 -*-
"""
    chat_parser.models
    ~~~~~~~~~~~~~~

    chat_parser models file

    :copyright: (c) 2014 by arruda.
"""

from django.db import models


class SomeModel(models.Model):
    """
    Some model descption
    """

    class Meta:
        app_label = 'chat_parser'
