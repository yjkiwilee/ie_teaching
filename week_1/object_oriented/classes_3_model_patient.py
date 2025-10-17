
class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation
    
class Doctor(Person):
    """
    A doctor managing multiple patients.

    Attributes:
        name (str): The name of the doctor.
        patients (list[Patient]): List of patients managed by this doctor.
    """

    def __init__(self, name: str, patients: list[Patient] = []):
        super().__init__(name)
        self.patients = patients

    def __str__(self):
        return self.name + ": " + ", ".join([
                patient.name for patient in self.patients
            ])
    
    def add_patient(self, patient: Patient) -> None:
        """
        Add a patient to the list of patients managed by the doctor.

        Parameters:
            patient (Patient): The patient instance to add to the list.
        
        Returns:
            None
        """

        # Check for pre-existence of patient
        assert patient.name not in [pt.name for pt in self.patients]

        # Add patient to list
        self.patients.append(patient)


        


alice = Patient('Alice')
print(alice)

obs = alice.add_observation(3)
print(obs)

bob = Person('Bob')
print(bob)

""" obs = bob.add_observation(4)
print(obs) """

charlotte = Doctor("Charlotte")

charlotte.add_patient(alice)

print(charlotte)