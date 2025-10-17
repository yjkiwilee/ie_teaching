"""Tests for the Patient model."""

import numpy as np
import numpy.testing as npt
import pytest
from inflammation.patient import Patient

# def test_create_patient():
#     """Test creating the patient."""

#     patient_id = 0
#     patient_data = np.array([1, 2, 3, 4])
    
#     test_patient = Patient(patient_id, patient_data)

#     npt.assert_equal(test_patient.id, patient_id)
#     npt.assert_array_equal(test_patient.data, patient_data)

# def test_daily_mean():
#     """Test the data_mean function."""

#     patient_data = np.array([1, 2, 3, 4])
    
#     test_patient = Patient(0, patient_data)

#     npt.assert_almost_equal(test_patient.data_mean(), 2.5, decimal=2)

# def test_daily_max():
#     """Test the data_max function."""

#     patient_data = np.array([1, 2, 3, 4])
    
#     test_patient = Patient(0, patient_data)

#     npt.assert_equal(test_patient.data_max(), 4)

# def test_daily_min():
#     """Test the data_min function."""

#     patient_data = np.array([1, 2, 3, 4])
    
#     test_patient = Patient(0, patient_data)

#     npt.assert_equal(test_patient.data_min(), 1)

class TestPatient:
    """Test for patient class."""
    
    def setup_class(self):
        self.patients = {
            1: Patient(1, np.array([1, 2, 3, 4])),
            2: Patient(2, np.array([5, 6, 7, 8]))
        }

    def test_patient_attributes(self):
        """Test that the patient attributes are set correctly."""
        
        assert self.patients[1].id == 1
        npt.assert_array_equal(self.patients[1].data, np.array([1, 2, 3, 4]))

    def test_daily_mean(self):
        """Test the data_mean function."""

        assert self.patients[1].data_mean() == 2.5

    def test_daily_max(self):
        """Test the data_max function."""

        assert self.patients[1].data_max() == 4

    def test_daily_min(self):
        """Test the data_min function."""

        assert self.patients[1].data_min() == 1