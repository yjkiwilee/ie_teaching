from abc import ABC, abstractmethod

class Person:
    """A person."""
    def __init__(self, name):
        self.name = name
        self.id = None

    def __str__(self):
        return self.name

    def set_id(self, id):
        raise NotImplementedError('set_id not implemented')

    def get_id(self):
        return self.id

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return 'Patient: ' + super().__str__()

    def set_id(self, id):
        self.id = 'P' + str(id).zfill(4)


class Doctor(Person):
    """A doctor in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return 'Doctor: ' + super().__str__()

    def set_id(self, id):
        self.id = 'D' + str(id).zfill(4)

class Trial:
    """
    A clinical trial.

    Attributes:
        people (list[Person]): List of people assigned to the trial.
    """

    def __init__(self, people: list[Person] = []):
        self.people = people

    def print_people(self):
        """
        Prints all the people in the room.
        
        Parameters:
            None

        Returns:
            None
        """

        print(
            ", ".join([str(person) for person in self.people])
        )

    def set_ids(self, ids: list[int]):
        """
        Set the IDs of people in the trial.

        Parameters:
            ids (list[int]): List of IDs to assign.

        Raises:
            AssertionError: If the list of IDs don't have the same length as the list of people
        """

        assert len(ids) == len(self.people)

        for person, new_id in zip(self.people, ids):
            person.set_id(new_id)

    def add_person(self, person):
        """
        Adds a person to the trial.
        
        Parameters:
            person (Person): Person to add.

        Returns:
            None

        Raises:
            TypeError: If the person doesn't have a get_id() function.
        """

        if not (hasattr(person, "get_id") and callable(person.get_id)):
            raise TypeError
        
        self.people.append(person)

alice = Patient('Alice')
print(alice)

bob = Person('Bob')
print(bob)

""" obs = bob.add_observation(4)
print(obs) """

charlotte = Doctor("Charlotte")
print(charlotte)

trial = Trial([alice])
trial.print_people()
trial.set_ids([1])
trial.add_person(charlotte)
trial.print_people()