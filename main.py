from utils import *
from state import *
import sys
import warnings
import numpy as np

warnings.filterwarnings('ignore')  # ignora tutti i warning
sns.set(style="darkgrid")          # setta lo stile dei grafici di seaborn


if __name__ == '__main__':
    flushOutput()
    folder_path = sys.argv[1]
    file_name = "BioSystem.mo"
    class_name = "BioSystem.Cell"

    # 0. Carico BioSystem.mo e per ogni specie creo un oggetto di tipo SpeciesParameter e per ogni rate..
    model = load_model(folder_path, file_name, class_name)
    params = [x["Name"] for x in model.getQuantities()]
    # undef = getUndefinedParameters(model)
    # rateParams = find_rate_params(undef)
    # speciesParams = find_species_params(undef)

    # 1. Per ogni parametro vado a cercarlo nel config.xml e setto i relativi amounts etc
    # for rateParam in rateParams:
        # trovalo in config.xml
        # se ha il valore di rate --> fixed = true
            # setta tale valore
        # altrimenti
            # fixed = false
            # aggiungilo a undefRateParams (su cui effettuiamo la search)
    # stessa cosa per gli speciesParams


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
