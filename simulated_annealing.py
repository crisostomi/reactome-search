import math, random
from node import Node


def cooling_rate(time):
    temp = 1 / (time + 1)
    return temp


def find_value(node):
    node.state.model.simulate()

    return node.state.model.getSolutions("mon.y")


def search(initial_state):
    time = 0
    current_node = Node(initial_state)
    adjacents = current_node.get_adjacents()

    while True:
        T = cooling_rate(time)
        if T == 0:
            return current_node

        next = random.choice(adjacents)

        value_difference = find_value(next) - find_value(current_node)
        if value_difference > 0:
            current_node = next
            adjacents = current_node.get_adjacents()
        else:
            prob = math.exp(value_difference / T)
            if random.random() <= prob:
                current_node = next
