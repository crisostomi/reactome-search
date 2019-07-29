
class RateParameter:

    def __init__(self, reaction_id):
        self.reaction_id = reaction_id
        self.min_rate = None
        self.max_rate = None
        self.rate = None
        self.fixed = None
