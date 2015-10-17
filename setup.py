import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import escargot 

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

requires = open('requirements.txt').read().strip().split('\n')
test_requires = requires + open('requirements-dev.txt').read().strip().split('\n')

setup(
    name = "escargot",
    version = escargot.__version__,
    author = "Vayel",
    author_email = "vincent.lefoulon@free.fr",
    packages = find_packages(),
    long_description = open('README.md').read(),
    install_requires = requires,
    include_package_data = True,
    url = "https://github.com/tartopum/Escargot",
    classifiers = [
        "Programming Language :: Python",
        "Natural Language :: French",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    licence = "MIT",
    cmdclass = {"test": PyTest},
    tests_require = test_requires
)
