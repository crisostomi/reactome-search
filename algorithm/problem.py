from algorithm.state import State
import copy

class Problem:

    def __init__(self, model, search_params):
        self.model = model
        self.search_params = search_params

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
        print([param for param, value in self.model.getParameters().items() if value is None])
        # self.model.simulate()
        return 1