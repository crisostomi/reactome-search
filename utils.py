import OMPython
import os
import pandas as pd                # dataframes
import matplotlib.pyplot as plt    # plottare grafici
import seaborn as sns              # si basa su plt, ha funzioni piu sofisticate
import shutil
import glob
import re
import xml.etree.ElementTree as ET
from SpeciesParameter import SpeciesParameter
from ReactionParameter import ReactionParameter


def load_model(folder_path, file_name, class_name):
    file_path = folder_path + file_name
    dependencies = ["Modelica"]
    for file in os.listdir(folder_path):
        if file.endswith(".mo") and not file == file_name:
            dependencies.append(folder_path + file)

    user_home = os.environ['HOME']
    dependencies.append(user_home + '/Dropbox/Tesisti/software/BioChem-1.0.1/BioChem/package.mo')
    dependencies.append(user_home + '/Dropbox/Tesisti/software/BioChem-1.0.1/new-models/reactions.mo')
    return OMPython.ModelicaSystem(file_path, class_name, dependencies)

def moveOutput():
    os.mkdir("./output")
    for file in glob.glob(r'./BioSystem*'):
        shutil.move(file, './output')

def flushOutput():
    shutil.rmtree('./output/', ignore_errors=True)


# Ritorna un oggetto Pandas DataFrame con all'interno i datapoints ({istante, valore}) delle variabili simulate del modello

def get_solutions(model, variables=[]):
    # recupera la "linea temporale"
    time = model.getSolutions("time")
    # se variables e' vuoto, mettici i nomi di tutte le variabili del sistema
    if len(variables) == 0:
        variables = model.getSolutions()

    # costruisce il dataframe con solo la prima variabile
    solutions = [model.getSolutions(var) for var in variables]
    df = pd.DataFrame({"time": time, "value": solutions[0], "variable": variables[0]})

    # appende al dataframe tutti i dati delle altre variabili
    for i in range(1, len(variables)):
        df = df.append(
            pd.DataFrame({"time": time, "value": solutions[i], "variable": variables[i]}),
            ignore_index=True
        )
    return df


# Prende in input un DataFrame pandas in cui vi sia la colonna "time", e una lista di variabili
# Plotta il moto delle variabili su un grafico in cui le ascisse sono l'asse del tempo e le ordinate l'asse dei valori
# ATTENZIONE: potrebbe perdere di significato se si cerca di plottare variabili in intervalli di valori di dimensione diversa

def plot_solutions(solution_frame, variables=[]):
    if len(variables) == 0:
        sns.lineplot(data=solution_frame, x="time", y="value", hue="variable")
    else:
        sns.lineplot(data=solution_frame[solution_frame['variable'].isin(variables)], x="time", y="value", hue="variable")
    plt.show()

# Ritorna una lista di nomi di parametri, i quali non sono definiti e a cui va assegnato un valore prima di simulare

def getUndefinedParameters(model):
    return [parameter for parameter,value in model.getParameters().items() if value is None]

def getSpeciesParameters(parsedConfigFile):
    return [ SpeciesParameter(species.get('id'), species.get('bounds_index'), species.get('init_index')) for species in parsedConfigFile.iter('species')]

def getRevReactionParameters(parsedConfigFile):
    return [ ReactionParameter(reaction.get('id'), True, reaction.get('k1_index'), reaction.get('k2_index')) for reaction in parsedConfigFile.iter('reversible')]

def getIrrevReactionParameters(parsedConfigFile):
    return [ ReactionParameter(reaction.get('id'), False, reaction.get('k1_index'), reaction.get('k2_index')) for reaction in parsedConfigFile.iter('irreversible')]

def getUndefinedSpeciesParams(speciesParams):
    return [ speciesParam for speciesParam in speciesParams if not speciesParam.fixed ]

def getUndefinedRevReactionParams(reactionParams):
    return [ speciesParam for speciesParam in reactionParams if (not speciesParam.fixed and speciesParam.reversible) ]

def getUndefinedIrrevReactionParams(reactionParams):
    return [ speciesParam for speciesParam in reactionParams if (not speciesParam.fixed and not speciesParam.reversible)]

def initializeIrrevReactionParams(reactionParams, configFileRoot):
    for reactionParam in reactionParams:
        for reaction in configFileRoot.iter('irreversible'):
            if reactionParam.reaction_id == reaction.get('id'):
                if reaction.get('k1') != '':
                    reactionParam.rate = reaction.get('k1')
                    reactionParam.fixed = True
                reactionParam.min_rate = reaction.get('min_k1')
                reactionParam.max_rate = reaction.get('max_k1')

def initializeRevReactionParams(reactionParams, parsedConfigFile):
    for reactionParam in reactionParams:
        for reaction in parsedConfigFile.iter('reversible'):
            if reactionParam.reaction_id == reaction.get('id'):
                reactionParam.reversible = True
                if (reaction.get('k1') != '') and (reaction.get('k2') != ''):
                    reactionParam.rate1 = reaction.get('k1')
                    reactionParam.rate2 = reaction.get('k2')
                    reactionParam.fixed = True
                reactionParam.min_rate1 = reaction.get('min_k1')
                reactionParam.max_rate1 = reaction.get('max_k1')
                reactionParam.min_rate2 = reaction.get('min_k2')
                reactionParam.max_rate2 = reaction.get('max_k2')


def initializeSpeciesParams(speciesParams, parsedConfigFile):
    for speciesParam in speciesParams:
        for species in parsedConfigFile.iter('species'):
            if speciesParam.species_id == species.get('id'):
                if species.get('initialAmount') != '':
                    speciesParam.initial_amount = species.get('initialAmount')
                    speciesParam.fixed = True
                speciesParam.min_amount = species.get('minAmount')
                speciesParam.max_amount = species.get('maxAmount')

def parseFile(file):
    tree = ET.parse(file)
    return tree.getroot()