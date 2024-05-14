"""
ja goede info
"""

from setuptools import setup, find_packages

setup(
    name="mymath",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version="0.1.0rc1",
    description="mymath",
    author="",
    entry_points={
    },
)
