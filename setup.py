#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme_file = path.join(path.dirname(path.abspath(__file__)), 'README.md')
try:
    from m2r import parse_from_file
    readme = parse_from_file(readme_file)
except ImportError:
    with open(readme_file) as f:
        readme = f.read()

install_requires = ['mistune', 'docutils']
test_requirements = ['pygments']

setup(
    name='m2r',
    version='0.3.1',
    description='Markdown and reStructuredText in a single file.',
    long_description=readme,
    author='Hiroyuki Takagi',
    author_email='miyako.dev@gmail.com',
    url='https://github.com/miyakogi/m2r',
    py_modules=['m2r'],
    entry_points={'console_scripts': 'm2r = m2r:main'},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='Markdown reStructuredText sphinx-extension',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
    ],
    install_requires=install_requires,
    test_suite='tests',
    tests_require=test_requirements,

)
