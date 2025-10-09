import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_example_from_prompt():
    """Test the primary example given in the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive_numbers():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5, -10]) == 0

def test_streak_at_the_beginning():
    """Test when the longest streak is at the start of the list."""
    assert longest_positive_streak([5, 6, 7, 0, 4, -2]) == 3

def test_streak_at_the_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7]) == 3

def test_multiple_streaks():
    """Test a list with multiple streaks to ensure the longest is chosen."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1, 2]) == 3

def test_single_positive_element():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_non_positive_element():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_identical_positive_numbers():
    """Test a streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_zeros_breaking_streaks():
    """Test that zeros correctly break streaks."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, 0, 6]) == 3

def test_negatives_breaking_streaks():
    """Test that negative numbers correctly break streaks."""
    assert longest_positive_streak([1, 2, -5, 3, 4, -1, 6, 7, 8]) == 3