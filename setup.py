from distutils.core import setup
from setuptools import find_packages


with open("README.rst", "r") as readme:
    README_TEXT = readme.read()

setup(
    name="dataclass-bakery",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    version="0.0.6",
    description="Dataclass Bakery offers you a smart way to create objects based on dataclasses for testing in Python",
    include_package_data=True,
    author="Miguel Jiménez",
    author_email="miguelflg13@gmx.com",
    url="https://github.com/miguelFLG13/dataclass-bakery",
    download_url="https://github.com/miguelFLG13/dataclass-bakery/tarball/0.0.6",
    long_description=README_TEXT,
    keywords="testing dataclass bakery",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
