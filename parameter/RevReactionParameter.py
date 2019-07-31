from parameter.ReactionParameter import ReactionParameter
import numpy as np


class RevReactionParameter(ReactionParameter):

    def __init__(self, id, compartment, k1_index, k2_index):
        super.__init__(id, compartment, k1_index)
        self.min_rate2 = None
        self.max_rate2 = None
        self.k2_index = k2_index

    def get_random_value_in_bounds(self):
        rand_k1 = np.random.uniform(self.min_rate1, self.max_rate1)
        rand_k2 = np.random.uniform(self.min_rate2, self.max_rate2)
        return rand_k1, rand_k2

    def initializeRevReactionParams(self, parsedConfigFile):
        for reaction in parsedConfigFile.iter('reversible'):
            if self.id == reaction.get('id'):
                self.reversible = True
                if (reaction.get('k1') != '') and (reaction.get('k2') != ''):
                    self.rate1 = reaction.get('k1')
                    self.rate2 = reaction.get('k2')
                    self.fixed = True
                self.min_rate1 = float(reaction.get('min_k1'))
                self.max_rate1 = float(reaction.get('max_k1'))
                self.min_rate2 = float(reaction.get('min_k2'))
                self.max_rate2 = float(reaction.get('max_k2'))

    def pass_parameter_to_model(self, model):
        super().pass_parameter_to_model(model)
        self.set_rate2_to_model(model)

    def set_rate2_to_model(self, model):
        param_name = self.compartment + ".const_k2[" + self.k2_index + "]"
        model.setParameters(**{param_name: self.rate2})

    def set_search_value(self, value):
        self.rate1 = value[0]
        self.rate2 = value[1]

    def get_search_value(self):
        return self.rate1, self.rate2