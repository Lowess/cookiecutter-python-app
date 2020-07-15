#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

# Extra requirements installable using pip -e '.[<extra>]'
EXTRAS_REQUIRE = {
    "docs": ["sphinx", "sphinxcontrib.mermaid>=0.3.1", "sphinx-rtd-theme>=0.4.3"],
    "tests": [
        "tox",
        "black",
        "coverage-badge>=1.0.1",
        "coverage>=5.0.3",
        "flake8>=3.7.9",
        "isort",
        "jellyfish>=0.7.2",
        "moto>=1.3.14",
        "nltk>=3.4.5",
        "pytest-cov>=2.8.1",
        "pytest-datafiles>=2.0",
        "pytest-env>=0.6.2",
        "pytest-logger>=0.5.1",
        "pytest-mock>=2.0.0",
        "pytest-runner>=5.2",
        "pytest-xdist>=1.31.0",
        "pytest>=5.2.2",
    ],
}

# Development requirements
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"] + ["pre-commit"]
)

setup(
    name="{{ cookiecutter.app_name }}",
    version="1.0.0",
    packages=["app"],
    extras_require=EXTRAS_REQUIRE,
)
