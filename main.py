from utils import *
from state import *
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

    speciesParams = getSpeciesParameters(parsedConfigFile)
    irrevReactionParams = getIrrevReactionParameters(parsedConfigFile)
    revReactionParams = getRevReactionParameters(parsedConfigFile)

    parsedKbFile = parseFile(kb_file)

    initializeSpeciesParams(speciesParams, parsedKbFile)
    initializeIrrevReactionParams(irrevReactionParams, parsedKbFile)
    initializeRevReactionParams(revReactionParams, parsedKbFile)

    undefSpeciesParams = getUndefinedSpeciesParams(speciesParams)
    undefIrrevReactionParams = getUndefinedIrrevReactionParams(irrevReactionParams)
    undefRevReactionParams = getUndefinedRevReactionParams(revReactionParams)

    # initial_state = State(folder_path, file_name, class_name)
    # undef = getUndefinedParameters(initial_state.model)
    # print(undef)
    # for param in undef:
    #     param_value = np.random.uniform(0, 1)
    #     initial_state.model.setParameters(**{param: param_value})
    #     print(param,param_value)
    # initial_state.model.setSimulationOptions(stopTime=20)
    # initial_state.model.simulate()
    # df = get_solutions(initial_state.model, ["c_1.reaction_1247665.k1"])
    # plot_solutions(df, ["c_1.reaction_1247665.k1"])
    moveOutput()
