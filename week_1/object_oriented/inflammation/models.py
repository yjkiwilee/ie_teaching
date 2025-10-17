from abc import ABC, abstractmethod

class Patient:
    """A patient in an inflammation study."""
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, value, day: int | None = None):
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1

            except IndexError:
                day = 0

        new_observation = {
            'day': day,
            'value': value,
        }

        self.observations.append(new_observation)
        return new_observation

alice = Patient('Alice')
print(alice)

observation = alice.add_observation(3)
print(observation)
print(alice.observations)