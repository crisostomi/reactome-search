
class Parameter:

    def __init__(self, id, compartment):
        self.id = id
        self.fixed = False
        self.compartment = compartment

    def is_fixed(self):
        return self.fixed

    def set_fixed(self, fixed):
        self.fixed = fixed

    def get_id(self):
        return self.id

    def pass_parameter_to_model(self, model):
        pass

    def initialize(self, file):
        pass

    def set_search_value(self, value):
        pass

    def get_search_value(self):
        pass

    def get_random_value_in_bounds(self):
        pass


    def __eq__(self, obj):
        return isinstance(obj, Parameter) and obj.id == self.id and obj.get_search_value() == self.get_search_value()