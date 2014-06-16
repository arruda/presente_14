# -*- coding: utf-8 -*-
"""
    Settings
    ~~~~~~~~~~~~~~

    A divided settings module.

    :copyright: (c) 2014 by arruda.
"""

import sys
import os


MAIN_APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_ROOT = os.path.dirname(MAIN_APP_ROOT)
SITE_ROOT = os.path.dirname(DJANGO_ROOT)
EMAILS_PATH = os.path.join(DJANGO_ROOT, 'char_parser', 'emails.html')
sys.path.append(DJANGO_ROOT)

SECRET_KEY = '35(!hyv2%=1zo!ly)ohlgx+iycffw(ioe6vg&l6x+(8r9x8tzi'

ON_PRODUCTION = os.environ.has_key('ON_PRODUCTION')

from config import *
from installed_apps import *
from logging import *

NO_DEPRECATION_WARNINGS=False
if not ON_PRODUCTION:
    NO_DEPRECATION_WARNINGS=True
    from env_dev import *
else:
    from env_prod import *

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)


