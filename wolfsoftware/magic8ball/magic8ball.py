"""
A Python module that emulates the classic Magic 8-Ball toy.

The Magic8Ball class provides randomized responses to yes/no questions in the traditional style of
a Magic 8-Ball, with 20 predefined answers classified into positive, neutral, and negative responses.

Usage:
    Run this script directly to interactively ask the Magic 8-Ball a question. Alternatively,
    import the `Magic8Ball` class into your project to incorporate the 8-Ball functionality.

Example:
    >>> from magic8ball import Magic8Ball
    >>> ball = Magic8Ball()
    >>> ball.ask_question("Will it rain tomorrow?")
    'Outlook good.'
"""

import random
from typing import Literal

from .exceptions import InvalidQuestionError


class Magic8Ball:
    """
    A Magic 8-Ball emulator class that provides randomized responses to yes/no questions.

    Attributes:
        responses (list of str): A list of possible Magic 8-Ball responses.
    """

    def __init__(self) -> None:
        """Initialise a Magic8Ball instance with standard responses."""
        self.responses: list[str] = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

    def ask_question(self, question: str) -> str:
        """
        Provide a Magic 8-Ball response to a yes/no question.

        Arguments:
            question (str): The question to be answered by the Magic 8-Ball.

        Returns:
            str: A randomly selected response from the Magic 8-Ball.

        Raises:
            InvalidQuestionError: If the question is empty or not a string.
        """
        if not isinstance(question, str) or not question.strip():
            raise InvalidQuestionError("Question must be a non-empty string.")
        return random.choice(self.responses)  # nosec - B311

    def __str__(self) -> Literal['Magic 8-Ball Emulator']:
        """
        Return a string representation of the Magic 8-Ball.

        Returns:
            str: A message indicating the object is a Magic 8-Ball emulator.
        """
        return "Magic 8-Ball Emulator"
