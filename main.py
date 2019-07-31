from algorithm.problem import Problem
from algorithm.state import *
from algorithm import simulated_annealing
import sys
import warnings
from utils.utils import *
from utils.modelica_utils import *
from utils.parameters_utils import *

warnings.filterwarnings('ignore')  # ignora tutti i warning
sns.set(style="darkgrid")          # setta lo stile dei grafici di seaborn


if __name__ == '__main__':
    flushOutput()
    folder_path = sys.argv[1]
    file_name = "BioSystem.mo"
    class_name = "BioSystem.Cell"

    model = load_model(folder_path, file_name, class_name)

    config_file = folder_path+"/config.xml"
    parsedConfigFile = parseFile(config_file)
    params = getParams(parsedConfigFile)

    kb_file = sys.argv[2]
    parsedKbFile = parseFile(kb_file)
    initializeParams(params, parsedKbFile)

    undefinedParams = getUndefinedParams(params)

    setFixedParams(model, params)

    problem = Problem(model, undefinedParams)


    step = 1 # float(sys.argv[3])
    treshold = 0.05 # float(sys.argv[4])
    result = simulated_annealing.search(problem, step, treshold)

    moveOutput()
