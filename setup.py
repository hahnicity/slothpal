
from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name='slothpal',
    version=__version__,
    description='A RESTful PayPal Python client',
    author='Gregory Rehm',
    author_email='grehm87@gmail.com',
    packages=find_packages(exclude=['*.tests']),
    setup_requires=[
    ],
    install_requires=[
        "requests>=1.2"
    ],
    tests_require=[
    ],
    test_suite='slothpal.tests',
)
