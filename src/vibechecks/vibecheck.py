"""The main VibeCheck class and its functionalities."""

from vibetools._internal import VibeLlmClient

from vibechecks.config.config import VibeCheckConfig
from vibechecks.utils.logger import console_logger


class VibeCheck:
    """
    A class that uses LLMs to perform "vibe checks" on statements or function calls.

    This class can be used as a decorator or as a function call to evaluate
    the logical validity of a statement or the outcome of a function call.
    """

    def __init__(
        self,
        client: VibeLlmClient,
        model: str,
        *,
        config: VibeCheckConfig | dict | None = None,
    ) -> None:
        """
        Initialize the VibeCheck object.

        Args:
            client: An instance of VibeLlmClient.
            model: The name of the model to use for the LLM.
            config: VibeCheckConfig containing runtime knobs (e.g., num_tries).

        """
        if config is None:
            config = VibeCheckConfig()
        elif isinstance(config, dict):
            config = VibeCheckConfig(**config)

        self.llm = VibeLlmClient(client, model, config, console_logger)

    def __call__(self, arg: str) -> bool:
        """
        Perform a vibe check on a string statement.

        Args:
            arg: A string statement to evaluate.

        Returns:
            A boolean indicating whether the statement is true or false.

        """
        return self.llm.vibe_eval(arg, bool)
