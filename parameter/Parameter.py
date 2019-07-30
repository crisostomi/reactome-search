
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

    def set_value_to_model(self, model):
        pass