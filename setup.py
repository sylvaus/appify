from setuptools import setup, find_packages

import appify

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="appify",
    version=appify.__version__,
    packages=find_packages(),
    url="https://github.com/sylvaus/appify",
    license="MIT",
    author="sylvaus",
    author_email="",
    description="Helpers to transform functions into CLI or simple UIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
