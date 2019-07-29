
class ReactionParameter:

    def __init__(self, reaction_id):
        self.reaction_id = reaction_id
        self.min_rate1 = None
        self.min_rate2 = None
        self.max_rate1 = None
        self.max_rate2 = None
        self.rate1 = None
        self.rate2 = None
        self.fixed = False
        self.name = None