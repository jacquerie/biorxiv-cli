# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import feedparser
import six


def feedparser_to_dict(obj):
    if isinstance(obj, feedparser.FeedParserDict) or isinstance(obj, dict):
        return {k: feedparser_to_dict(v) for k, v in six.iteritems(obj)}
    elif isinstance(obj, list):
        return [feedparser_to_dict(el) for el in obj]
    return obj
