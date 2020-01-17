import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    'Topic :: Software Development :: Libraries :: Python Modules'
]

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='kth-timeoutdecorator',
    version='0.0.3',
    description='timeout decorator for python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Angel Hair',
    author_email='asdwsl@foxmail.com',
    url='https://github.com/Angel-Hair/kth-timeoutdecorator',
    packages=['kth_timeoutdecorator'],
    install_requires=[],
    classifiers=CLASSIFIERS)