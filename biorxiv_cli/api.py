# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import feedparser
import requests

from .config import READ_BASE_URL
from .errors import BiorxivAPIDown
from .utils import feedparser_to_dict


class Client(object):
    def read(self, subjects):
        if not subjects:
            subjects = ('all',)

        response = requests.get(READ_BASE_URL + '+'.join(subjects))
        if not response.ok:
            raise BiorxivAPIDown()

        parsed_response = feedparser.parse(response.content)
        dict_response = feedparser_to_dict(parsed_response)

        return dict_response['entries']
