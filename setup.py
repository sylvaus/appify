import codecs
import os.path

from setuptools import setup, find_packages


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="appify",
    version=get_version("appify/__init__.py"),
    packages=find_packages(),
    url="https://github.com/sylvaus/appify",
    license="MIT",
    author="sylvaus",
    author_email="",
    description="Helpers to transform functions into CLI or simple UIs",
    long_description=read("readme.md"),
    long_description_content_type="text/markdown",
    extras_require={
        "test": ["pytest>=5.4.2", "pytest-cov>=2.9.0", "tox>=3.15.1"],
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
