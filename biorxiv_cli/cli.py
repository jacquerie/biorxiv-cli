# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import click

from .api import Client
from .config import READ_CATEGORIES


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx):
    ctx.obj = Client()


@cli.command()
@click.argument('subjects', nargs=-1, type=click.Choice(READ_CATEGORIES))
@click.pass_obj
def read(client, subjects):
    """Read the 30 most recent posts.

    Will print the titles of the 30 most recent posts in one of the
    comma-separated subjects. By default assumes that all subjects
    were selected.
    """
    for i, entry in enumerate(client.read(subjects), 1):
        number = click.style('{}.  '.format(str(i).rjust(4)), fg='yellow')
        title = click.style(entry['title'], bold=True)
        click.echo(number + title)
