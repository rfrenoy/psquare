# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='psquare',
    version='1.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    author='Rémy Frenoy',
    author_email='rfrenoy@gmail.com',
    description='This is a Python implementation of the p-square algorithm',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rfrenoy/psquare",
    install_requires=[
        'numpy'
    ],
    extras_require={
        'example': ['matplotlib']
    }
)
