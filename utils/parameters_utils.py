from parameter.SpeciesParameter import SpeciesParameter
from parameter.ReactionParameter import ReactionParameter
from parameter.RevReactionParameter import RevReactionParameter
from parameter.VolumeParameter import VolumeParameter


def getParams(parsedConfigFile):
    return getSpeciesParameters(parsedConfigFile) + \
           getRevReactionParameters(parsedConfigFile) + \
           getIrrevReactionParameters(parsedConfigFile) + \
           getVolumeParameters(parsedConfigFile)

def getVolumeParameters(parsedConfigFile):
    return [VolumeParameter(0, 0, is_cell=True)] + \
           [VolumeParameter(
               comp.get('id'),
               comp.get('id')
           )
               for comp in parsedConfigFile.iter('compartment')]

def getSpeciesParameters(parsedConfigFile):
    return [ SpeciesParameter(species.get('id'),
                              species.get('bounds_index'),
                              species.get('init_index'),
                              species.get('compartment')
                              )
             for species in parsedConfigFile.iter('species')]

def getRevReactionParameters(parsedConfigFile):
    return [ RevReactionParameter(reaction.get('id'),
                                  reaction.get('k1_index'),
                                  reaction.get('k2_index'),
                                  reaction.get('compartment')
                                  )
             for reaction in parsedConfigFile.iter('reversible')]

def getIrrevReactionParameters(parsedConfigFile):
    return [ ReactionParameter(reaction.get('id'),
                               reaction.get('k1_index'),
                               reaction.get('compartment')
                               )
             for reaction in parsedConfigFile.iter('irreversible')]


def getUndefinedParams(params):
    return [ param for param in params if param.fixed == False ]

def initializeParams(params, parsed_kb):
    for param in params:
        param.initialize(parsed_kb)

def setFixedParams(model, params):
    for param in params:
        if param.is_fixed():
            param.pass_parameter_to_model(model)