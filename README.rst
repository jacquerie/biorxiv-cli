=============
 bioRxiv-CLI
=============

.. image:: https://travis-ci.org/jacquerie/biorxiv-cli.svg?branch=master
    :target: https://travis-ci.org/jacquerie/biorxiv-cli

.. image:: https://coveralls.io/repos/github/jacquerie/biorxiv-cli/badge.svg?branch=master
    :target: https://coveralls.io/github/jacquerie/biorxiv-cli?branch=master


About
=====

A Python wrapper for the bioRxiv API.


Install
=======

.. code-block:: console

    $ pip install biorxiv-cli


Usage
=====

You can use ``bioRxiv-CLI`` as a CLI to navigate bioRxiv or as a library to
query its API.

CLI
---

Currently ``bioRxiv-CLI`` implements one subcommand:

.. code-block:: console

    $ biorxiv read SUBJECTS

This will print the titles of the 30 most recent posts in one of the
comma-separated subjects. For example:

.. image:: https://raw.githubusercontent.com/jacquerie/biorxiv-cli/master/images/biorxiv-cli-screen.png

If no subjects were given, it will assume by default that all subjects
were selected.

API
---

The previous CLI is built on top of a Python library that can be used on its
own to query bioRxiv's API. For example:

.. code-block:: python

    >>> from biorxiv_cli import Client
    >>> client = Client()
    >>> client.read([SUBJECTS])

will achieve the same effect as

.. code-block:: console

    $ biorxiv read SUBJECTS


Author
======

Jacopo Notarstefano (`@Jaconotar`_)

.. _`@Jaconotar`: https://twitter.com/Jaconotar


License
=======

MIT
