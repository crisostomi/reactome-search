from parameter.Parameter import Parameter


class VolumeParameter(Parameter):

    def __init__(self, id, compartment, is_cell=False):
        super().__init__(id, compartment)
        super().set_fixed(True)
        self.volume_percentage = None
        self.volume = None
        self.is_cell = is_cell

    def initialize(self, parsedConfigFile):
        if not self.is_cell:
            for comp in parsedConfigFile.iter('compartment'):
                if self.id == comp.get('id'):
                    self.volume_percentage = float(comp.get('vol_percentage'))
        else:
            self.volume = parsedConfigFile.iter('cell').__next__().get('volume')

    def pass_parameter_to_model(self, model):
        if self.is_cell:
            self.pass_cell_V_to_model(model)
        else:
            self.pass_vol_percentage_to_model(model)

    def pass_cell_V_to_model(self, model):
        param_name = "cell_V"
        model.setParameters(**{param_name: self.volume})

    def pass_vol_percentage_to_model(self, model):
        param_name = self.compartment + ".vol_percentage"
        model.setParameters(**{param_name: self.volume_percentage})