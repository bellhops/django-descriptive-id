#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import meta_mixin

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = meta_mixin.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-descriptive-id',
    version=version,
    description="""Human-readable, unique ID field mixing""",
    long_description=readme + '\n\n' + history,
    author='Bellhops',
    author_email='tech@getbellhops.com',
    url='https://github.com/bellhops/django-descriptive-id',
    include_package_data=True,
    install_requires=[
        'django',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-descriptive-id',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
