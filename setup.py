from __future__ import with_statement
from setuptools import setup

setup(
    name='osx_launch_cleaner',
    version='0.1',
    description='Tool to assist in tracking down launched daemons',
    url='https://github.com/ryantownshend/osx_launch_cleaner',
    author='Ryan Townshend',
    py_modules=['osx_launch_cleaner'],
    install_requires=[
        'click>=6.6',
        'click-log>=0.1.4',
    ],
    entry_points={
        'console_scripts': [
            'olc = osx_launch_cleaner:main',
        ],
    },

)
