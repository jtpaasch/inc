"""The ``setup.py`` file for the package."""

from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="inc",
    version="1.0.0",
    description="A tableaux prover.",
    long_description=long_description,
    packages=find_packages(
        exclude=["venv", "tests"]
    ),
    entry_points={
        "console_scripts": [
            "inc = inc.cli.main:cli"
        ],
    },
)
