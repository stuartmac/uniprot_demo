============
UniProt Demo
============


.. image:: https://img.shields.io/pypi/v/uniprot_demo.svg
        :target: https://pypi.python.org/pypi/uniprot_demo

.. image:: https://img.shields.io/travis/stuartmac/uniprot_demo.svg
        :target: https://travis-ci.com/stuartmac/uniprot_demo

.. image:: https://readthedocs.org/projects/uniprot-demo/badge/?version=latest
        :target: https://uniprot-demo.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




UniProt Demo highlights some of the features of the UniProt API and dsome useful analyses with the available data.


* Free software: MIT license
* Documentation: https://uniprot-demo.readthedocs.io.


Features
--------

* TODO

Installation
============

To install the module, run:

.. code-block:: bash

   pip install .

Usage
=====

You can use this module as a library in your Python code:

.. code-block:: python

   from uniprot_demo import get_protein_domains

   uniprot_id = "P12345"
   domains_df = get_protein_domains(uniprot_id)
   print(domains_df)

You can also use it as a command line tool:

.. code-block:: bash

   uniprot-domains P12345

Configuration
=============

You can customize the configuration by creating a `config.json` file with the following content:

.. code-block:: json

   {
     "cache_expiration_seconds": 3600
   }

Then, set the `MY_UNIPROT_MODULE_CONFIG` environment variable to the path of the custom configuration file.

Tests
=====

To run the tests, execute:

.. code-block:: bash

   python -m unittest discover tests

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
