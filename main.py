from state import *


if __name__ == '__main__':
    folder_path = os.getcwd() + "/test"
    file_name = "BioSystem.mo"
    class_name = "BioSystem.Cell"
    initial_state = State(folder_path, file_name, class_name)
    print(initial_state.model.getParameters())
