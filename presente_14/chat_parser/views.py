# -*- coding: utf-8 -*-
"""
    chat_parser.views
    ~~~~~~~~~~~~~~

    chat_parser views file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to