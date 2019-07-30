from parameter.SpeciesParameter import SpeciesParameter
from parameter.ReactionParameter import ReactionParameter
from parameter.RevReactionParameter import RevReactionParameter


def getParams(parsedConfigFile):
    return getSpeciesParameters(parsedConfigFile) + getRevReactionParameters(parsedConfigFile) + getIrrevReactionParameters(parsedConfigFile)

def getSpeciesParameters(parsedConfigFile):
    return [ SpeciesParameter(species.get('id'), species.get('bounds_index'), species.get('init_index'), species.get('compartment')) for species in parsedConfigFile.iter('species')]

def getRevReactionParameters(parsedConfigFile):
    return [ RevReactionParameter(reaction.get('id'), reaction.get('k1_index'), reaction.get('k2_index'), reaction.get('compartment')) for reaction in parsedConfigFile.iter('reversible')]

def getIrrevReactionParameters(parsedConfigFile):
    return [ ReactionParameter(reaction.get('id'), reaction.get('k1_index'), reaction.get('compartment')) for reaction in parsedConfigFile.iter('irreversible')]


def getUndefinedParams(params):
    return [ param for param in params if param.fixed == False ]

def initializeParams(params, configFileRoot):
    for param in params:
        param.initialize(configFileRoot)

def setFixedParams(model, params):
    for param in params:
        if param.is_fixed():
            param.set_value_to_model(model)