"""Your project's description"""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='sqlsplit',
    description="A project that does things!",
    version='0.1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    author='Avram Lyon',
    author_email='ajlyon@gmail.com',
    url='https://github.com/ajlyon/sqlsplit',
    license='Apache 2.0',
    install_requires=requirements
)
