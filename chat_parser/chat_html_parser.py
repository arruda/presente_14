#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys


if __name__ == "__main__" and __package__ is None:

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(1, parent_dir)

    mod = __import__('chat_parser')
    sys.modules["chat_parser"] = mod
    __package__ = 'chat_parser'

    from .html_parser import get_emails_html

    html = get_emails_html()
    print len(html)
