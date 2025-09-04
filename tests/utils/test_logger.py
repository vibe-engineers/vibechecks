"""Tests for the logger utility."""

import logging

from vibechecks.utils.logger import console_logger


def test_console_logger():
    """Test that console_logger is a configured logging.Logger instance."""
    assert isinstance(console_logger, logging.Logger)
    assert console_logger.name == "VibeChecks"
