
class ReactionParameter:

    def __init__(self, reaction_id, reversible, k1_index):
        self.reaction_id = reaction_id
        self.min_rate1 = None
        self.min_rate2 = None
        self.max_rate1 = None
        self.max_rate2 = None
        self.rate1 = None
        self.rate2 = None
        self.fixed = False
        self.reversible = reversible
        self.name = None
        self.k1_index = k1_index

    def __init__(self, reaction_id, reversible, k1_index, k2_index):
        self.reaction_id = reaction_id
        self.min_rate1 = None
        self.min_rate2 = None
        self.max_rate1 = None
        self.max_rate2 = None
        self.rate1 = None
        self.rate2 = None
        self.fixed = False
        self.reversible = reversible
        self.name = None
        self.k1_index = k1_index
        self.k2_index = k2_index