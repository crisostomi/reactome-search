from algorithm.state import *
from utils.modelica_utils import get_solutions
import copy

from parameter.SpeciesParameter import *


class Problem:

    def __init__(self, model, search_params):
        self.model = model
        self.search_params = search_params
        self.species_params = [param for param in search_params if isinstance(param, SpeciesParameter)]

    def get_initial_state(self):
        initial_search_params = copy.deepcopy(self.search_params)
        for initial_search_param in initial_search_params:
            new_val = initial_search_param.get_random_value_in_bounds()
            initial_search_param.set_search_value(new_val)
        initial_state = State(initial_search_params)
        return initial_state

    def find_value(self, state):
        for search_param in state.search_params:
            search_param.pass_parameter_to_model(self.model)
        self.model.simulate()
        unhappiness_value = self.find_monitor_value()
        return -1 * unhappiness_value

    def find_monitor_value(self):
        return sum([self.find_species_monitor_value(species_param)
                    for species_param in self.species_params])

    def find_species_monitor_value(self, species_param):
        monitor_name = "mon." + species_param.id + "_monitor"
        monitor = get_solutions(self.model, [monitor_name])

        print(monitor)

        monitor_value = monitor['value'].iloc[-1]


        return monitor_value