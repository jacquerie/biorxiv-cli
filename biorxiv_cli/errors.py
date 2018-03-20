# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class BiorxivError(Exception):
    pass


class BiorxivAPIDown(BiorxivError):
    pass
