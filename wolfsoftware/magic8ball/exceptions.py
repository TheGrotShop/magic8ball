"""
This module defines custom exceptions.

Classes:
    - Magic8BallError: A custom exception class with a default error message.
    - InvalidQuestionError: A custom exceptions class for invalid questions.
"""


class Magic8BallError(Exception):
    """Custom exception class for Magic8Ball-related errors."""

    pass


class InvalidQuestionError(Magic8BallError):
    """Exception raised for invalid questions."""

    def __init__(self, message="Question must be a non-empty string.") -> None:
        """Initialise the class."""
        self.message: str = message
        super().__init__(self.message)
