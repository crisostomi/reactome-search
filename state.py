from OMPython import ModelicaSystem
import os


def load_model(folder_path, file_name, class_name):
    file_path = folder_path + "/" + file_name
    dependencies = ["Modelica"]
    for file in os.listdir(folder_path):
        if file.endswith(".mo") and not file == file_name:
            dependencies.append(folder_path + "/" + file)
    return ModelicaSystem(file_path, class_name, dependencies)


class State:

    def __init__(self, model):
        self.model = model
        self.quality = 0

    def __init__(self, folder_path, file_name, class_name):
        self.model = load_model(folder_path, file_name, class_name)

    def get_undefined_parameters(self):
        return [param for param, value in self.model.getParameters().items() if value is None]

    def get_adjacents(self, step):
        adjs = []
        undef = self.model.getParameters(self.get_undefined_parameters())

        # come troviamo i vicini?

        return adjs
