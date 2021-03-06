#!/usr/bin/env python
import os, sys
from setuptools import setup


package_dir = os.path.join(os.path.dirname(__file__), 'mcu_info_util')
data_files = []
for root, dirs, files in os.walk(os.path.join(package_dir, 'metadata')):
    data_files += [os.path.join(root, file) for file in files]
data_files = [os.path.relpath(data_file, package_dir) for data_file in data_files]


setup(
    name='mcu-info-util',
    version='0.2',
    author='Ivan Kolesnikov',
    author_email='kiv.apple@gmail.com',
    url='https://github.com/KivApple/mcu-info-util',
    packages=['mcu_info_util'],
    package_dir={'mcu_info_util': 'mcu_info_util'},
    package_data={'mcu_info_util': data_files},
    data_files=[('share/mcu-info-util', ['misc/rules.mk', 'misc/toolchain.cmake'])],
    entry_points={
        'console_scripts': [
            'mcu-info-util = mcu_info_util.__main__:main'
        ]
    },
    install_requires=[
        'six'
    ]
)
