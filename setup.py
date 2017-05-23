"""
appnexus-client
"""

import os
import subprocess
import sys
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_dependencies(requirements):
    with open(requirements) as requirement_file:
        lines = requirement_file.readlines()
    dependencies = map(lambda line: line.split('=')[0], lines)
    return list(dependencies)

setup(
    name="cleaner",
    version="0.3.0",
    author="Alexandre Bonnetain",
    author_email="alexandrebonnetain@gmail.com",
    description="Clean your repositories with a cool interactive shell",
    long_description=read("README.rst"),
    url="https://github.com/shir0kamii/cleaner",
    download_url="https://github.com/shir0kamii/cleaner/tags",
    platforms="any",
    packages=find_packages(),
    install_requires=get_dependencies("requirements.txt"),
    entry_points={
        'console_scripts': [
            'cleaner = cleaner.cli:run_cleaner'
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Environment :: Console",
        "Topic :: System :: Filesystems",
        "Topic :: System :: Shells",
        "Programming Language :: Python :: 3.5",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
