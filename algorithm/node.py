
class Node:
    def __init__(self, state):
        self.state = state

    def get_adjacents(self, step):
        return [Node(state) for state in self.state.get_adjacents(step)]
