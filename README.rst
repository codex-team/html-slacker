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
    '*Hello*, _Slack_!'

Test it.

.. code:: python

    $ python setup.py test


Requirements
------------

- Python >= 2.5
- html

Links
-----

Repository: https://github.com/codex-team/html-slacker

Report a bug: https://github.com/codex-team/html-slacker/issues

PyPI Package: https://pypi.python.org/pypi/html-slacker

CodeX Team: https://ifmo.su
