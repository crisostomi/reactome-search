import numpy as np
from parameter.Parameter import Parameter

class ReactionParameter(Parameter):

    def __init__(self, id, k1_index, compartment):
        super().__init__(id, compartment)
        self.min_rate1 = None
        self.max_rate1 = None
        self.rate1 = None
        self.k1_index = k1_index

    def get_random_value_in_bounds(self):
        rand_k1 = np.random.uniform(self.min_rate1, self.max_rate1)
        return rand_k1

    def initialize(self, configFileRoot):
        for reaction in configFileRoot.iter('irreversible'):
            if self.id == reaction.get('id'):
                if reaction.get('k1') != '':
                    self.rate1 = float(reaction.get('k1'))
                    self.fixed = True
                self.min_rate1 = float(reaction.get('min_k1'))
                self.max_rate1 = float(reaction.get('max_k1'))

    def pass_parameter_to_model(self, model):
        self.set_rate1_to_model(model)

    def set_rate1_to_model(self, model):
        param_name = self.compartment + ".const_k1[" + str(self.k1_index) + "]"
        model.setParameters(**{param_name: self.rate1})

    def set_search_value(self, value):
        self.rate1 = value

    def get_search_value(self):
        return self.rate1
