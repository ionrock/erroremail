#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = []

setup(
    name='erroremail',
    version='0.1.3',
    description='Send an error email when an you get an exception.',
    long_description=readme,
    author='Eric Larson',
    author_email='eric@ionrock.org',
    url='https://github.com/ionrock/erroremail',
    packages=[
        'erroremail',
    ],
    package_dir={'erroremail':
                 'erroremail'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='erroremail',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
