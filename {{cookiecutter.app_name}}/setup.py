#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Setup requirements
try:
    from setuptools import find_packages, setup
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
        "tox>=3.25.0,<4",
        "black>=22.6.0,<23",
        "coverage-badge>=1.1.0",
        "coverage>=6.4.1",
        "flake8>=4.0.1,<5",
        "isort>=5.10.1,<6",
        "moto>=3.1.16,<4",
        "pytest-cov>=3.0.0,<4",
        "pytest-datafiles>=2.0.1,<3",
        "pytest-env>=0.6.2,<1",
        "pytest-logger,=0.5.1,<1",
        "pytest-mock>=3.8.1,<4",
        "pytest-runner>=6.0.0,<7",
        "pytest-xdist>=2.5.0<3",
        "pytest-lazy-fixture>=0.6.3,<1",
        "pytest-sugar>=0.9.4,<1",
        "pytest>=7.1.2,<8",
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
