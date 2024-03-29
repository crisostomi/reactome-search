import numpy as np
from parameter.Parameter import Parameter

class SpeciesParameter(Parameter):

    def __init__(self, id, monitorIndex, initIndex, compartment):
        super().__init__(id, compartment)
        self.initial_amount = None
        self.min_amount = None
        self.max_amount = None
        self.monitorIndex = monitorIndex
        self.initIndex = initIndex

    def get_random_value_in_bounds(self):
        return np.random.uniform(self.min_amount, self.max_amount)

    def initialize(self, parsedConfigFile):
        for species in parsedConfigFile.iter('species'):
            if self.id == species.get('id'):
                if species.get('initialAmount') != '':
                    self.initial_amount = species.get('initialAmount')
                    self.fixed = True
                self.min_amount = float(species.get('minAmount'))
                self.max_amount = float(species.get('maxAmount'))

    def pass_parameter_to_model(self, model):
        self.pass_initial_amount_to_model(model)
        self.pass_monitor_to_model(model)

    def pass_initial_amount_to_model(self, model):
        param_name = self.compartment + ".init[" + self.initIndex + "]"
        model.setParameters(**{param_name: self.initial_amount})

    def pass_monitor_to_model(self, model):
        param_name_min = "mon." + "minAmount[" + self.monitorIndex + "]"
        param_name_max = "mon." + "maxAmount[" + self.monitorIndex + "]"
        model.setParameters(**{param_name_min: self.min_amount, param_name_max: self.max_amount})

    def set_search_value(self, value):
        self.initial_amount = value

    def get_search_value(self):
        return self.initial_amount