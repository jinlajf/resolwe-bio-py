.. _tutorial:

===============
Getting started
===============

This tutorial is for bioinformaticians. It will help you install the SDK
and showcase some basic commands. We will connect to a Resolwe server,
upload a BAM file, and identify a chromosome with the most aligned
reads. Before we begin, make sure you have SSH access to the
`Torta server`_.

.. _Torta server: https://torta.bcm.genialis.com

Installation
============

Installing is easy, just make sure you have Python_ and pip_ installed
on your computer. Run this command in the terminal (CMD on Windows)::

  pip install resdk

.. _Python: https://www.python.org/downloads/
.. _pip: https://pip.pypa.io/en/stable/installing/

.. warning::

   If you use macOS, be aware that the version of `Python shipped with the
   system doesn't support TLSv1.2`_, which is required for connecting to
   any ``genialis.com`` server (and probably others). To solve the issue,
   install the latest version of Python 2.7 or Python 3 `via official
   installer from Python.org`_ or `with Homebrew`_.

.. _`Python logging`: https://docs.python.org/2/howto/logging.html
.. _`Python shipped with the system doesn't support TLSv1.2`:
    http://pyfound.blogspot.si/2017/01/time-to-upgrade-your-python-tls-v12.html
.. _`via official installer from Python.org`:
    https://www.python.org/downloads/mac-osx/
.. _`with Homebrew`:
    http://docs.python-guide.org/en/latest/starting/install/osx/

Registration
============

Examples in documentation require access to a public Resolwe server.
You can use a public Resolwe server `Genialis Platform`_ that is
configured for the examples in tutorial. Some parts of the
documentation will work for registered users only. Please
`create an account`_ on Genialis Platform before you continue,
and remember your username and password.

.. _`Genialis Platform`: https://app.genialis.com
.. _`create an account`: https://app.genialis.com/rna-seq/user/create_account

Query data
==========

Run Python interpreter (type ``python`` in the terminal) and connect
to the Resolwe server:

.. literalinclude:: files/example_index.py
   :lines: 1-7

TODO:

* Explain what is data and how to get data from Genialis Platform
  (copy the relevant text from the current Getting started).
* Query a genome and a read data object.
* Inspect both objects.

Run alignment
=============

TODO:

* Explain what are processes (copy the relevant text from the current Getting started)
* Run alignment (hisat2) on the reads and the genome we have queried in the previous step
* Inspect the alignment results
* List the other alignment methods and give a links to the reference section
