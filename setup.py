import os

from setuptools import setup


def read(fname):
    fullname = os.path.join(os.path.dirname(__file__), fname)
    with open(fullname) as fp:
        content = fp.read()
    return content


setup(
    name="cleaner",
    version="0.4.0",
    url="https://github.com/Shir0kamii/cleaner",
    author_email="shir0kamii@gmail.com",
    description="Cleaner is a cool interactive shell that allows you to "
                "clean your directories with less eforts.",
    long_description=read("README.rst"),
    download_url="https://github.com/Shir0kamii/cleaner/tags",
    platforms="any",
    packages=["cleaner"],
    install_requires=[
        "clize>=3.0"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ],
    entry_points={
        "console_scripts": [
            "cleaner = cleaner.cli:run_cleaner"
        ],
    },
)
