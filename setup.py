#!/usr/bin/env python

from setuptools import setup, find_packages
import SCFpy
import os


def extra_dependencies():
    import sys
    ret = []
    if sys.version_info < (2, 7):
        ret.append('argparse')
    return ret


def read(*names):
    values = dict()
    extensions = ['.txt', '.rst']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values

long_description = """
%(README)s
News
====
%(CHANGES)s
""" % read('README', 'CHANGES')

setup(
    name='SCFpy',
    version=SCF.__version__,
    description='Simple restrited Hatree-Fock code',
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: beginners of computational chemistry",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Computational chemistry",
    ],
    keywords='Simple restrited Hatree-Fock code',
    author='Pu Du',
    author_email='rocketsboy@gmail.com',
    maintainer='Pu Du',
    maintainer_email='rocketsboy@gmail.com',
    url='https://github.com/pudu1991/SCFpy',
    license='GNU',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'howdoi = SCFpy.main:command_line_runner',
        ]
    },
    install_requires=[
        'numpy',
    ] + extra_dependencies(),
)