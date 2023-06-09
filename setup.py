#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Atabek De Murtaza",
    author_email='atabekdemurtaza@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This web app provides multiple choices for delivery on the similar situation i.e foods, gadgets",
    entry_points={
        'console_scripts': [
            'food=food.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='food',
    name='food',
    packages=find_packages(include=['food', 'food.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/atabekdemurtaza/DeliverApp',
    version='0.1.0',
    zip_safe=False,
)
