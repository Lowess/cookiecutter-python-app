#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Setup requirements
try:
    from setuptools import setup, find_packages
    from setuptools.command.install import install
except ImportError:
    print(
        "setuptools is needed in order to build. Install it using your package manager (usually python-setuptools) or via pip (pip install setuptools)."
    )
    sys.exit(1)

# Extra requirements installable using pip -e '.[<extra>]'
EXTRAS_REQUIRE = {
    "docs": ["sphinx<4.0.0", "sphinxcontrib.mermaid==0.6.1", "sphinx-rtd-theme>=0.4.3"],
    "tests": [
        "tox",
        "black>=20.8b1,<21",
        "click>7.0",
        "coverage-badge>=1.0.1",
        "coverage>=5.0.3",
        "flake8>=3.7.9",
        "isort>=5.6.0,<5.7.0",
        "moto==1.3.16.dev122",  # See https://github.com/spulec/moto/pull/3466
        "pytest-cov>=2.8.1",
        "pytest-datafiles>=2.0",
        "pytest-env>=0.6.2",
        "pytest-logger>=0.5.1",
        "pytest-mock>=2.0.0",
        "pytest-runner>=5.2",
        "pytest-xdist>=1.31.0",
        "pytest-lazy-fixture>=0.6.3,<0.7",
        "pytest-sugar>=0.9.4",
        "pytest>=5.2.2",
    ],
}

# Development requirements
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"]
    + EXTRAS_REQUIRE["docs"]
    + ["pre-commit", "colorlog<5.1.0"]
)

setup(
    name="{{ cookiecutter.app_name }}",
    version="1.0.0",
    package_dir={"": "."},
    packages=find_packages(),
    package_data={"": ["*.toml"]},
    extras_require=EXTRAS_REQUIRE,
)
