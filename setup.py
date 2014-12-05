"""A simple flask server for splitting SQL code into queries."""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='sqlsplit',
    description="A server for splitting sql using sqlformat",
    version='0.1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    author='Avram Lyon',
    author_email='avram@scopely.com',
    url='https://github.com/scopely/sqlsplit',
    license='Apache 2.0',
    install_requires=requirements
)
