import numpy as np
from Parameter import Parameter

class SpeciesParameter(Parameter):

    def __init__(self, id, monitorIndex, initIndex, compartment):
        super().__init__(id, compartment)
        self.initial_amount = None
        self.min_amount = None
        self.max_amount = None
        self.amount = None
        self.name = None
        self.monitorIndex = monitorIndex
        self.initIndex = initIndex

    def get_random_value_in_bounds(self):
        return np.random.uniform(self.min_amount, self.max_amount)
