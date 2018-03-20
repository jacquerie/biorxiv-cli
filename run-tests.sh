# -*- coding: utf-8 -*-

set -e

flake8 biorxiv_cli tests
py.test tests
