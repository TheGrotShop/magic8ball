"""
This test module provides unit tests for the File Size Converter module using pytest.
It includes tests for versioning, name retrieval, and size conversion functions.
"""

import pytest
from wolfsoftware.magic8ball import Magic8Ball, InvalidQuestionError


def test_ask_question_returns_response() -> None:
    """Test that a valid question returns a response."""
    magic_ball = Magic8Ball()
    response: str = magic_ball.ask_question("Will I pass my test?")
    assert response in magic_ball.responses, "The response should be one of the standard Magic 8-Ball answers."  # nosec: B101


def test_ask_question_randomness() -> None:
    """Test that multiple calls to ask_question return various possible responses."""
    magic_ball = Magic8Ball()
    responses: set[str] = {magic_ball.ask_question("Will I succeed?") for _ in range(100)}
    # Assert we get multiple unique responses in the set
    assert len(responses) > 1, "The responses should vary across multiple calls."  # nosec: B101


def test_invalid_question_empty_string() -> None:
    """Test that an empty question raises an InvalidQuestionError."""
    magic_ball = Magic8Ball()
    with pytest.raises(InvalidQuestionError, match="Question must be a non-empty string."):
        magic_ball.ask_question("")


def test_invalid_question_non_string() -> None:
    """Test that a non-string question raises an InvalidQuestionError."""
    magic_ball = Magic8Ball()
    with pytest.raises(InvalidQuestionError, match="Question must be a non-empty string."):
        magic_ball.ask_question(42)


def test_str_method() -> None:
    """Test the __str__ method returns the correct string representation."""
    magic_ball = Magic8Ball()
    assert str(magic_ball) == "Magic 8-Ball Emulator", "The __str__ method should return 'Magic 8-Ball Emulator'."  # nosec: B101
