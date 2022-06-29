#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
from logging.config import dictConfig

from dynaconf import LazySettings

# Configure Dynaconf
settings = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF="APP_{{ cookiecutter.app_name | upper }}",
    ENVVAR_FOR_DYNACONF="APP_SETTINGS",
)


dictConfig(settings.LOGGING)

logger = logging.getLogger(__package__)

# Show loaded config
config = settings.as_dict()
if settings.get("CONFIG_PRETTYPRINT", False):
    config = json.dumps(settings.as_dict(), indent=2)

logger.info(
    f"Microservice initialized for ({settings.current_env} env) with: " f"{config}"
)
