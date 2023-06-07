#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'pandas', 'requests', 'requests-cache', ]

test_requirements = [ ]

setup(
    author="Stuart Alexander MacGowan",
    author_email='smacgowan@dundee.ac.uk',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="UniProt Demo highlights some of the features of the UniProt API and dsome useful analyses with the available data.",
    entry_points={
        'console_scripts': [
            'uniprot_demo=uniprot_demo.cli:main',
            "uniprot-domains=uniprot_demo.cli:main"
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='uniprot_demo',
    name='uniprot_demo',
    packages=find_packages(include=['uniprot_demo', 'uniprot_demo.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/stuartmac/uniprot_demo',
    version='0.1.0',
    zip_safe=False,
)
