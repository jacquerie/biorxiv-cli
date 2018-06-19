# -*- coding: utf-8 -*-

"""A Python wrapper for the bioRxiv API."""

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup


url = 'https://github.com/jacquerie/biorxiv-cli'

readme = open('README.rst').read()

setup_requires = [
    'autosemver~=0.0,>=0.5.3',
]

install_requires = [
    'click~=6.0,>=6.7',
    'feedparser~=5.0,>=5.2.1',
    'requests~=2.0,>=2.18.4',
    'six~=1.0,>=1.11.0',
]

docs_require = []

tests_require = [
    'flake8-future-import~=0.0,>=0.4.4',
    'flake8~=3.0,>=3.5.0',
    'pytest-cov~=2.0,>=2.5.1',
    'pytest-vcr~=0.0,>=0.3.0',
    'pytest~=3.0,>=3.4.2',
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name not in ['all']:
        extras_require['all'].extend(reqs)

packages = find_packages(exclude=['docs'])

setup(
    name='biorxiv-cli',
    autosemver={
        'bugtracker_url': url + '/issues',
    },
    url=url,
    license='MIT',
    author='Jacopo Notarstefano',
    author_email='jacopo.notarstefano@gmail.com',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    description=__doc__,
    long_description=readme,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'biorxiv = biorxiv_cli.cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
