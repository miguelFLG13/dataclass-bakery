from distutils.core import setup
from setuptools import find_packages


with open("README.rst", "r") as readme:
    README_TEXT = readme.read()

setup(
    name="dataclass-bakery2",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests", "tests.*"]),
    version="1.0.0",
    description="Dataclass Bakery offers you a smart way to create objects based on dataclasses for testing in Python",
    include_package_data=True,
    author="Miguel Jiménez",
    author_email="miguelflg13@gmx.com",
    url="https://github.com/miguelFLG13/dataclass-bakery",
    download_url="https://github.com/miguelFLG13/dataclass-bakery/tarball/1.0.0",
    long_description=README_TEXT,
    long_description_content_type="text/x-rst",
    keywords="testing dataclass bakery",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    python_requires=">=3.10",
)
