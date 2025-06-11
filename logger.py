"""Unified logging utilities for the project."""

from __future__ import annotations

import logging
from logging import Logger
from typing import Optional


def setup_logger(
    name: str = "zero_system",
    *,
    level: int = logging.INFO,
    log_file: Optional[str] = "zero_system.log",
) -> Logger:
    """Return a configured :class:`logging.Logger` instance."""

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.setLevel(level)
    return logger


logger: Logger = setup_logger()

