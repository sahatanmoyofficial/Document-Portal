"""
Setup script for the Document Portal package.
"""

from setuptools import setup, find_packages

setup(
    name="Document Portal",
    author="Tanmoy Saha",
    version="0.1",
    packages=find_packages(exclude=["tests*", "examples*"])
)