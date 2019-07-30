
class SpeciesParameter:

    def __init__(self, species_id, boundsIndex, initIndex):
        self.species_id = species_id
        self.initial_amount = None
        self.min_amount = None
        self.max_amount = None
        self.amount = None
        self.fixed = None
        self.name = None
        self.boundsIndex = boundsIndex
        self.initIndex = initIndex


