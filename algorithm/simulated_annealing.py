import math, random
from algorithm.node import Node


def cooling_rate(time):
    temp = 1 / (time + 1)
    return temp

def search(problem, step, treshold):
    time = 0
    current_node = Node(problem.get_initial_state())
    while True:
        T = cooling_rate(time)
        if T < treshold:
            return current_node
        adjacents = current_node.get_adjacents(step)
        next = random.choice(adjacents)
        value_difference = problem.find_value(next.state) - problem.find_value(current_node.state)
    #     if value_difference > 0:
    #         current_node = next
    #     else:
    #         prob = math.exp(value_difference / T)
    #         if random.random() <= prob:
    #             current_node = next
        time += 1


