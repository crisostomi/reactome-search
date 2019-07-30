import numpy as np


class ReactionParameter:

    def __init__(self, id, reversible, k1_index, compartment, k2_index=None):
        super.__init__(id, compartment)
        self.min_rate1 = None
        self.min_rate2 = None
        self.max_rate1 = None
        self.max_rate2 = None
        self.rate1 = None
        self.rate2 = None
        self.reversible = reversible
        self.name = None
        self.k1_index = k1_index
        self.k2_index = k2_index

    def get_random_value_in_bounds(self):
        rand_k1 = np.random.uniform(self.min_rate1, self.max_rate1)
        if self.reversible:
            rand_k2 = np.random.uniform(self.min_rate2, self.max_rate2)
            return rand_k1, rand_k2
        else:
            return rand_k1