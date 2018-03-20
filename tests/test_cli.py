# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest

from biorxiv_cli.cli import cli


@pytest.mark.vcr()
def test_read_accepts_one_subject(runner):
    result = runner.invoke(cli, ['read', 'biochemistry'])

    assert 0 == result.exit_code
    assert 'Influence of SNF1' in result.output


@pytest.mark.vcr()
def test_read_accepts_multiple_subjects(runner):
    result = runner.invoke(cli, ['read', 'genomics', 'bioinformatics'])

    assert 0 == result.exit_code
    assert 'SISS-Geo' in result.output


@pytest.mark.vcr()
def test_read_falls_back_to_all_without_subjects(runner):
    result = runner.invoke(cli, ['read'])

    assert 0 == result.exit_code
    assert 'Neurodynamic explanation' in result.output
