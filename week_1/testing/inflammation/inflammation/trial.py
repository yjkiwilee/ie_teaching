import numpy as np

from inflammation.patient import Patient

class Trial:
    """
    Class for storing all data in a clinical trial.

    Attributes:
        id: Trial ID
        data: Trial data
    """

    def __init__(self, trial_id, trial_data):
        self.id = trial_id
        self.data = trial_data

    @classmethod
    def from_csv(cls, trial_id, trial_fname):
        """
        Create trial data from a CSV file

        Parameters:
            trial_id (int): ID of the trial
            trial_fname (str): Path to the CSV file

        Returns:
            trial (Trial): Trial instance containing the data from the CSV file
        """

        return cls(
            trial_id,
            np.loadtxt(fname=trial_fname, delimiter=',')
        )

    def daily_mean(self):
        """Calculate the daily mean of a 2d inflammation data array."""
        return np.mean(self.data, axis=0)

    def daily_max(self):
        """Calculate the daily max of a 2d inflammation data array."""
        return np.max(self.data, axis=0)

    def daily_min(self):
        """Calculate the daily min of a 2d inflammation data array."""
        return np.min(self.data, axis=0)

    def patient_normalise(self):
        """
        Normalise patient data from a 2D inflammation data array.

        NaN values are ignored, and normalised to 0.

        Negative values are rounded to 0.

        If the maximal inflammation value is negative, all returned values are rounded to 0.
        """

        # Check if the data is a Numpy ndarray
        if not isinstance(self.data, np.ndarray):
            raise TypeError('Data should be a Numpy ndarray')
        
        # Check that the data is a 2d-array
        if self.data.ndim != 2:
            raise ValueError('Data should be a 2-dimentional array')

        # Check if the data contains negative values
        if np.any(self.data < 0):
            raise ValueError('Inflammation values should not be negative')

        # If data is an empty column array, just return the given data
        if self.data.shape[0] == 0 or self.data.shape[1] == 0:
            return self.data

        max_data = np.nanmax(self.data, axis=1)
        with np.errstate(invalid='ignore', divide='ignore'):
            normalised = self.data / max_data[:, np.newaxis]
        normalised[np.isnan(normalised)] = 0
        normalised[normalised < 0] = 0
        return normalised

    def get_patient(self, i):
        """
        Get the ith patient as a Patient object.
        """

        return Patient(i, self.data[i, :])