# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cslshoes/__init__.py
from cslshoes import __version__ as version

setup(
	name='cslshoes',
	version=version,
	description='CSL Shoes Custom App',
	author='Bhavik Patel',
	author_email='bhavikpatel7023@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
