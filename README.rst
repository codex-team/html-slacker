html-slacker
============

Converts HTML to Slack formatted markdown

Usage
-----

Install HTMLSlacker from pip.

.. code:: bash

    $ pip install html-slacker

Import library.

.. code:: python

    >>> from htmlslacker import HTMLSlacker

Use it.

.. code:: python

    >>> HTMLSlacker('<b>Hello</b>, <i>Slack</i>!').get_output()
    '*Hello*,_Slack_!'

Requirements
------------

- Python >= 2.5
- html

Links
-----

Repository: https://github.com/codex-bot/html-slacker

Report a bug: https://github.com/codex-bot/html-slacker/issues

PyPI Package: https://pypi.python.org/pypi/html-slacker

CodeX Team: https://ifmo.su
