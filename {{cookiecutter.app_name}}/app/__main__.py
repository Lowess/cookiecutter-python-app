#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from app.exit import GracefulExit
from prometheus_client import start_http_server

logger = logging.getLogger(f"app.{__name__}")

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(8000)

    killer = GracefulExit()

    try:
        while not killer.kill_now:
            logger.info("Hello from Microservice")
            killer.exit_gracefully(1, None)
    except Exception:
        logger.exception("Microservice faced an unrecoverable exception")

    logger.info("Shutting down microservice...")
    # cleanup before exit if needed.
    logger.info("Microservice gracefully shutdown!")
