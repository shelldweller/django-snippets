#!/usr/bin/env python

from distutils.core import setup

from snippets import VERSION


setup(
    name='Django snippets',
    version=VERSION,
    description='django-snippets enables content managers to maintain small chunks of text embedded in other web pages',
    author='shelldweller',
    url='https://github.com/shelldweller/django-snippets',
    packages=['snippets','snippets.templatetags'],
    data_files=[
        ('snippets/locale/uk/LC_MESSAGES', ['snippets/locale/uk/LC_MESSAGES/django.mo',
                                            'snippets/locale/uk/LC_MESSAGES/django.po'])
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
    ],
)