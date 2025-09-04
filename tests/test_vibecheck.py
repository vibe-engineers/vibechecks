"""Tests for the VibeCheck class."""

from unittest.mock import Mock, patch

import pytest

from vibechecks.utils.logger import console_logger
from vibechecks.vibecheck import VibeCheck


@pytest.fixture
def mock_vibe_llm_client():
    """Fixture to mock the VibeLlmClient."""
    with patch("vibechecks.vibecheck.VibeLlmClient") as mock_client:
        yield mock_client


def test_vibecheck_init(mock_vibe_llm_client: Mock):
    """Test the __init__ method of VibeCheck."""
    mock_llm_instance = Mock()
    mock_vibe_llm_client.return_value = mock_llm_instance

    client = Mock()
    model = "test-model"
    config = {"num_tries": 3}

    vibe_check = VibeCheck(client, model, config=config)

    mock_vibe_llm_client.assert_called_once_with(
        client, model, config, console_logger
    )
    assert vibe_check.llm is mock_llm_instance


def test_vibecheck_call(mock_vibe_llm_client: Mock):
    """Test the __call__ method of VibeCheck."""
    mock_llm_instance = Mock()
    mock_llm_instance.vibe_eval.return_value = True
    mock_vibe_llm_client.return_value = mock_llm_instance

    vibe_check = VibeCheck(Mock(), "test-model")

    statement = "is the sky blue?"
    result = vibe_check(statement)

    mock_llm_instance.vibe_eval.assert_called_once_with(statement, bool)
    assert result is True


def test_vibecheck_call_false(mock_vibe_llm_client: Mock):
    """Test the __call__ method of VibeCheck when vibe_eval returns False."""
    mock_llm_instance = Mock()
    mock_llm_instance.vibe_eval.return_value = False
    mock_vibe_llm_client.return_value = mock_llm_instance

    vibe_check = VibeCheck(Mock(), "test-model")

    statement = "is the sky green?"
    result = vibe_check(statement)

    mock_llm_instance.vibe_eval.assert_called_once_with(statement, bool)
    assert result is False