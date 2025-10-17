"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

@pytest.mark.parametrize(
    'test, expected',
    [
        ([[1, 4, 9], [3, 7, 1], [8, 6, 3]], [8, 7, 9]),
        ([[2, 8, 4], [3, 7, 1], [7, 6, 3]], [7, 8, 4]),
    ])
def test_daily_max_integers(test, expected):
    """Test that the daily max functions works for an array of positive integers."""
    from inflammation.models import daily_max

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    'test, expected',
    [
        ([[7, 1, 5], [3, 7, 9], [8, 6, 1]], [3, 1, 1]),
        ([[2, 8, 4, 10], [3, 7, 1, 6], [7, 6, 3, 1]], [2, 6, 1, 1]),
    ])
def test_daily_min_integers(test, expected):
    """Test that the daily max functions works for an array of positive integers."""
    from inflammation.models import daily_min

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

""" @pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
        ([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([], []),
        ([[], []], [[], []]),
        ([[1, 1, np.nan], [1, 1, 1], [1, 1, 1]], [[1, 1, 0], [1, 1, 1], [1, 1, 1]]),
    ]) """
@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        (
            np.array([[-1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            None,
            ValueError,
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
            None,
        ),
        (
            'Foo',
            None,
            TypeError
        ),
        (
            np.array([1, 2, 3, 4]),
            None,
            ValueError,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(test), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(test), np.array(expected), decimal=2)