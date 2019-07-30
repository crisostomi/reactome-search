from utils import *
from algorithm.state import *
import sys
import warnings


warnings.filterwarnings('ignore')  # ignora tutti i warning
sns.set(style="darkgrid")          # setta lo stile dei grafici di seaborn


if __name__ == '__main__':
    flushOutput()
    folder_path = sys.argv[1]
    file_name = "BioSystem.mo"
    class_name = "BioSystem.Cell"
    config_file = sys.argv[2]
    kb_file = sys.argv[3]
    model = load_model(folder_path, file_name, class_name)

    parsedConfigFile = parseFile(config_file)

    params = getParams(parsedConfigFile)

    parsedKbFile = parseFile(kb_file)

    initializeParams(params, parsedKbFile)

    undefinedParams = getUndefinedParams(params)

    setFixedParams(model, params)

    modelParams = model.getParameters()

    moveOutput()
