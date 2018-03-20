# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest
from click.testing import CliRunner


@pytest.fixture(scope='function')
def runner():
    return CliRunner()
