#!/usr/bin/env python

from setuptools import setup
from stratum import version

classifiers = [
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Topic :: Communications',
    'Environment :: Console',
]

install_requires = [
    'autobahn',
    'ecdsa',
    'PyOpenSSL',
    'twisted',
    'setuptools',
]

extras_require = {
    'mysql': ['PyMySQL'],
    'postgres': ['psycopg2'],
}

setup(
    name='stratum',
    version=version.VERSION,
    description='Stratum server implementation based on Twisted',
    author='slush',
    author_email='info@bitcion.cz',
    maintainer='Lane Shaw',
    maintainer_email='lshaw.tech@gmail.com',
    platforms='OS Independent (Written in an interpreted language)',
    license='GNU General Public License v3 or later (GPLv3+)',
    url='http://blog.bitcoin.cz/stratum',
    packages=['stratum'],
    package_dir={'stratum': 'stratum'},
    zip_safe=True,
    classifiers=classifiers,
    install_requires=install_requires,
    extras_require=extras_require,
)
