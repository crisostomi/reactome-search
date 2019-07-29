from utils import *
from state import *
import sys
import warnings
import numpy as np
from SpeciesParameter import SpeciesParameter
from ReactionParameter import ReactionParameter
import xml.etree.ElementTree as ET


warnings.filterwarnings('ignore')  # ignora tutti i warning
sns.set(style="darkgrid")          # setta lo stile dei grafici di seaborn


if __name__ == '__main__':
    flushOutput()
    folder_path = sys.argv[1]
    file_name = "BioSystem.mo"
    class_name = "BioSystem.Cell"


    model = load_model(folder_path, file_name, class_name)
    params = [param["Name"] for param in model.getQuantities()]

    speciesParams = [ SpeciesParameter(speciesParam) for speciesParam in getSpeciesParameters(params)]
    reactionParams = [ ReactionParameter(reactionParam) for reactionParam in getReactionParameters(params)]

    tree = ET.parse(sys.argv[2])
    root = tree.getroot()


    undefSpeciesParams = []
    undefReactionParams = []

    for speciesParam in speciesParams:
        for species in root.iter('species'):
            if speciesParam.species_id == species.get('id'):
                if species.get('initialAmount') != '':
                    speciesParam.initial_amount = species.get('initialAmount')
                    reactionParam.fixed = True
                else:
                    undefSpeciesParams.append(speciesParam)
                speciesParam.min_amount = species.get('minAmount')
                speciesParam.max_amount = species.get('maxAmount')

    for reactionParam in reactionParams:
        for reaction in root.iter('irreversible'):
            if reactionParam.reaction_id == reaction.get('id'):
                if reaction.get('k1') != '':
                    reactionParam.rate = reaction.get('k1')
                    reactionParam.fixed = True
                else:
                    undefReactionParams.append(reactionParam)
                reactionParam.min_rate = reaction.get('min_k1')
                reactionParam.max_rate = reaction.get('max_k1')

    for reactionParam in reactionParams:
        for reaction in root.iter('reversible'):
            if reactionParam.reaction_id == reaction.get('id'):
                if (reaction.get('k1') != '') and (reaction.get('k2') != ''):
                    reactionParam.rate1 = reaction.get('k1')
                    reactionParam.rate2 = reaction.get('k2')
                    reactionParam.fixed = True
                else:
                    undefReactionParams.append(reactionParam)
                reactionParam.min_rate1 = reaction.get('min_k1')
                reactionParam.max_rate1 = reaction.get('max_k1')
                reactionParam.min_rate2 = reaction.get('min_k2')
                reactionParam.max_rate2 = reaction.get('max_k2')

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
