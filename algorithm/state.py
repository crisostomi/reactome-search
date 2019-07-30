import copy

class State:

    def __init__(self, search_params):
        self.search_params = search_params

    def get_adjacents(self, step):
        adjs = []

        for index, search_param in enumerate(self.search_params):
            # incremento
            increased_assign = copy.deepcopy(self.search_params)
            increased_param = copy.deepcopy(search_param)
            increased_param.set_search_value(increased_param.get_search_value() + step)
            increased_assign.remove(search_param)
            increased_assign.insert(index, increased_param)
            adjs.append(State(increased_assign))

            # decremento
            decreased_assign = copy.deepcopy(self.search_params)
            decreased_param = copy.deepcopy(search_param)
            decreased_param.set_search_value(decreased_param.get_search_value() - step)
            decreased_assign.remove(search_param)
            decreased_assign.insert(index, decreased_param)
            adjs.append(State(decreased_assign))

        return adjs

