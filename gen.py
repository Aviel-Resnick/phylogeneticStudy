import random
from constants import *

def genSeq(len):
    seq = ""

    for i in range(0, len):
        seq = seq + str(random.choice(bases))
    return seq

def evolve(sequence, mutations, mutationCode):
    for x in range(0, mutations):
        #mutationCode = random.randint(0, 2)
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

def main():
    # generate root seq of given length
    root = genSeq(rootLength)
    print("Root:         " + root)
    print("Addition:     " + evolve(root, 1, 0))
    print("Deletion:     " + evolve(root, 1, 1))
    print("substitution: " + evolve(root, 1, 2))

main()
