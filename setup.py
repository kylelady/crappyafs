#!/usr/bin/env python

from distutils.core import setup

setup(name='crapPyAFS',
        version='1.0',
        description='PyAFS implemented with fork-and-execs',
        author='Kyle Lady',
        author_email='kylelady@umich.edu',
        url='https://github.com/kylelady/crappyafs',
        classifiers=['Programming Language :: Python',
                'Topic :: System :: Filesystems',],
        packages=['afs',],)
