from utils import *

class State:

    def __init__(self, model):
        self.model = model

    def __init__(self, folder_path, file_name, class_name):
        self.model = load_model(folder_path, file_name, class_name)

    def get_undefined_parameters(self):
        return [param for param, value in self.model.getParameters().items() if value is None]

    def get_adjacents(self, step):
        adjs = []
        undef = self.model.getParameters(self.get_undefined_parameters())

        # come troviamo i vicini?

        return adjs
