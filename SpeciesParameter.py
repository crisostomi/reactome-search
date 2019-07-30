import numpy as np


class SpeciesParameter:

    def __init__(self, species_id, monitorIndex, initIndex):
        self.species_id = species_id
        self.initial_amount = None
        self.min_amount = None
        self.max_amount = None
        self.amount = None
        self.fixed = None
        self.name = None
        self.monitorIndex = monitorIndex
        self.initIndex = initIndex

    def get_random_value(self):
        return np.random.uniform(self.min_amount, self.max_amount)
