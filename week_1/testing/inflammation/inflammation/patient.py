import numpy as np

class Patient:
    """
    Class for the data associated with a patient.

    Attributes:
        id: ID of the patient
        data: List containing inflammation scores recorded
    """

    def __init__(self, patient_id, data = np.array([])):
        self.id = patient_id
        self.data = data

    def data_mean(self):
        """
        Calculate the mean inflammation score for the patient.

        Parameters:

        Returns:
            mean_score: Mean inflammation score
        """

        return np.mean(self.data)

    def data_max(self):
        """
        Calculate the max inflammation score for the patient.
        NaNs in the data are ignored.

        Parameters:

        Returns:
            max_score: Max inflammation score
        """

        return np.nanmax(self.data)

    def data_min(self):
        """
        Calculate the min inflammation score for the patient.
        NaNs in the data are ignored.

        Parameters:

        Returns:
            min_score: Max inflammation score
        """

        return np.nanmin(self.data)
