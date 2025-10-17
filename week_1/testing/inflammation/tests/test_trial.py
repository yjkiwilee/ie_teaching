"""Test the functionailities of the Trial class."""

import pytest
import numpy as np
import numpy.testing as npt
from inflammation.trial import Trial

@pytest.fixture(scope="session")
def trial_1():
    return Trial(1, "data/inflammation-01.csv")

class TestTrial:
    def test_daily_mean_zeros(self, trial_1):
        """Test that mean function works for an array of zeros."""

        trial_1.data = np.array([[0, 0],
                                [0, 0],
                                [0, 0]])
        test_result = np.array([0, 0])

        # Need to use Numpy testing functions to compare arrays
        npt.assert_array_equal(trial_1.daily_mean(), test_result)


    def test_daily_mean_integers(self, trial_1):
        """Test that mean function works for an array of positive integers."""

        trial_1.data = np.array([[1, 2],
                            [3, 4],
                            [5, 6]])
        test_result = np.array([3, 4])

        # Need to use Numpy testing functions to compare arrays
        npt.assert_array_equal(trial_1.daily_mean(), test_result)

    def test_daily_max_integers(self, trial_1):
        """Test that the daily max functions works for an array of positive integers."""
        
        trial_1.data = np.array([[1, 4, 9], [3, 7, 1], [8, 6, 3]])
        test_result = np.array([8, 7, 9])

        # Need to use Numpy testing functions to compare arrays
        npt.assert_array_equal(trial_1.daily_max(), test_result)
    
    def test_daily_min_integers(self, trial_1):
        """Test that the daily max functions works for an array of positive integers."""
        
        trial_1.data = np.array([[2, 8, 4, 10], [3, 7, 1, 6], [7, 6, 3, 1]])
        test_result = np.array([2, 6, 1, 1])

        # Need to use Numpy testing functions to compare arrays
        npt.assert_array_equal(trial_1.daily_min(), test_result)

    def test_daily_min_string(self, trial_1):
        """Test for TypeError when passing strings"""

        trial_1.data = np.array([['Hello', 'there'], ['General', 'Kenobi']])

        with pytest.raises(TypeError):
            trial_1.data(min())

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
    def test_patient_normalise(self, test, expected, expect_raises, trial_1):
        """Test normalisation works for arrays of one and positive integers."""

        trial_1.data = test

        if expect_raises is not None:
            with pytest.raises(expect_raises):
                npt.assert_almost_equal(trial_1.patient_normalise(), np.array(expected), decimal=2)
        else:
            npt.assert_almost_equal(trial_1.patient_normalise(), np.array(expected), decimal=2)
