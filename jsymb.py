import sys
from math import prod
import itertools as it

class Subnode:
    def __init__(self):
        self.arc = None
        self.chord = None
        self.visited = None


class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.prev = Subnode()
        self.next = Subnode()


if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise ValueError("second argument needed: chord diagram's code.")

    word = sys.argv[1]
    symbols = list(set(word))

    word_valid = True

    for s in symbols:
        if word.count(s) != 2:
            word_valid = False

    if not word_valid:
        raise ValueError("second argument must be a string containing exactly two instances of each character.")

    nodes = []

    n_nodes = len(word)
    n = int(n_nodes / 2)

    for i, c in enumerate(word):

        if i == 0:

            new = Node(c)
            nodes.append(new)

        if 0 < i < n_nodes - 1:

            new = Node(c)
            nodes.append(new)

            old = nodes[i - 1]
            new.prev.arc = old.next
            old.next.arc = new.prev

        if i == n_nodes - 1:

            new = Node(c)
            nodes.append(new)

            old = nodes[i - 1]
            new.prev.arc = old.next
            old.next.arc = new.prev

            origin = nodes[0]
            new.next.arc = origin.prev
            origin.prev.arc = new.next

    chord_map = {}
    for i, w in enumerate(word):
        for j, x in enumerate(word):
            if w == x and i != j:
                chord_map[i] = j


    def connected_components(nodelist):
        ccs = 0

        for node in nodelist:

            if node.next.visited == True:
                continue

            charted = False
            curr = node.next

            while not charted:

                if curr.visited:
                    charted = True
                    ccs += 1

                elif not curr.visited:
                    curr.visited = True
                    curr = curr.arc.chord

        return ccs


    cuml = 0
    for state in it.product([1, 2], repeat=n):

        # Smooth according to state
        for i, node in enumerate(nodes):

            if state[symbols.index(node.symbol)] == 1:
                node.next.chord = nodes[chord_map[i]].prev
                node.prev.chord = nodes[chord_map[i]].next

            elif state[symbols.index(node.symbol)] == 2:
                node.prev.chord = node.next
                node.next.chord = node.prev

        # Set all unvisited
        for node in nodes:
            node.next.visited = False
            node.prev.visited = True


        ccs = connected_components(nodes)
        product = prod(state)

        cuml += product * (-2) ** (ccs - 1)
    

    print(cuml)
