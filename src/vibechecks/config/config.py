"""Configuration objects for VibeCheck."""

from typing import Any

from vibetools._internal import VibeConfig


class VibeCheckConfig(VibeConfig):
    """
    Configuration for VibeCheck, extending the base VibeConfig.

    This configuration sets a default system instruction for the LLM.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the VibeCheckConfig object.

        Args:
            *args: Positional arguments to pass to the parent VibeConfig.
            **kwargs: Keyword arguments to pass to the parent VibeConfig.
                      'system_instruction' is given a default value.

        """
        kwargs.setdefault(
            "system_instruction",
            "Evaluate the statement below and respond with either 'True' or 'False'.",
        )

        super().__init__(*args, **kwargs)
