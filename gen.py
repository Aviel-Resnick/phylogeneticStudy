import random
from constants import *
from dispTree import *

def genSeq(len):
    seq = ""

    for i in range(0, len):
        seq = seq + str(random.choice(bases))
    return seq

def evolve(sequence, mutations):
    for x in range(0, mutations):
        mutationCode = random.randint(0, 2)
        # frameshift addition
        if (mutationCode == 0):
            spot = random.randint(0, len(sequence))
            sequence = sequence[:spot] + str(random.choice(bases)) + sequence[spot:]
        # frameshift deletion
        if (mutationCode == 1):
            spot = random.randint(0, len(sequence))
            sequence = sequence[:spot] + sequence[spot+1:]
        # substitution / point mutation
        if (mutationCode == 2):
            spot = random.randint(0, len(sequence) - 1)
            old = sequence[spot]
            new = str(random.choice(bases))
            while(old == new):
                new = str(random.choice(bases))
            sequence = sequence[:spot] + new + sequence[spot+1:]
    return sequence

def genTree(root):
    tree = []
    tree.append(root)
    children = random.randint(0,3)
    for i in range(0, children):
        tree.append(evolve(root, random.randint(1,3)))
    return tree

def main():
    # generate root seq of given length
    root = genSeq(rootLength)
    print("Root:         " + root)
    #tree = genTree(root)
    tree = ["Root",["G", "H"]]
    print("Tree:       " + str(tree))
    drawtree(tree, (0,120), 1)

main()
