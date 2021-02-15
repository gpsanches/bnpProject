# -*- coding: utf-8 -*-

from .prod import *

try:
    from .local import *
except ImportError:
    pass
