"""Quandles are algebraic structures (Q, *) with the following properties:
1. For all a in Q, a * a = a
2. For all a, b in Q, there exists a unique c in Q such that a * c = b
3. For all a, b, c in Q, a * (b * c) = (a * b) * (a * c)
"""
from itertools import permutations, product
import pickle
import random

def check_imdempotence(cayley_table):
    for i in range(len(cayley_table)):
        if cayley_table[i][i] != i:
            return False
    return True

def check_distributivity(cayley_table):
    for i in range(len(cayley_table)):
        for j in range(len(cayley_table)):
            for k in range(len(cayley_table)):
                if cayley_table[i][cayley_table[j][k]] != cayley_table[cayley_table[i][j]][cayley_table[i][k]]:
                    return False
    return True

def check_if_quandle(cayley_table):
    if not check_imdempotence(cayley_table):
        return False

    if not check_distributivity(cayley_table):
        return False
    return True

def gen_quandles(order, limit=10**7):
    quandles = []
    # test all combinations of columns, colums are permutations of the order
    # At first, start with the identity permutation in all columns
    # Then test all permutations of the order

    i = 0
    for cayley in product(permutations(range(order)), repeat=order):
        # Transpose the table
        cayley = list(map(list, zip(*cayley)))
        i += 1
        if check_if_quandle(cayley):
            print_quandle(cayley)
            quandles.append(cayley)
        
        if i > limit:
            break

    # Save the quandles to a file
    pickle.dump(quandles, open(f"quandles_{order}.p", "wb"))
    return quandles

def gen_random_quandle(order):
    # Generate a random quandle
    cayley = [[0 for i in range(order)] for j in range(order)]
    # For each column, generate a random permutation
    rows = list(permutations(range(order)))
    for i in range(order):
        cayley[i] = random.choice(rows)

    cayley = list(map(list, zip(*cayley)))


    if check_if_quandle(cayley):
        return cayley
    
def random_quandle(order, limit=10**6):
    quandles = pickle.load(open(f"quandles_{order}.p", "rb"))
    i = 0
    while i < limit:
        cayley_table = gen_random_quandle(order)
        if cayley_table is not None:
            print_quandle(cayley_table)
            # quandles.append(cayley_table)
        i += 1
    pickle.dump(quandles, open(f"quandles_{order}.p", "wb"))
    return quandles


def print_quandle(cayley_table):
    for i in range(len(cayley_table)):
        # Make the table look nice
        row = ""
        for j in range(len(cayley_table)):
            row += str(cayley_table[i][j]) + " "
        print(row)
    print()

def load_quandles(order):
    # Use pickle to load the quandles from a file
    return pickle.load(open(f"quandles_{order}.p", "rb"))

def main():
    order = 3
    random.seed(1)
    gen_quandles(order)

def test():
    # Test the quandle properties
    cayley_table = [[0, 0, 0, 0], [2, 1, 1, 1], [1, 2, 2, 2], [3, 3, 3, 3]]
    print_quandle(cayley_table)
    print(check_imdempotence(cayley_table))
    print(check_distributivity(cayley_table))
    print(check_if_quandle(cayley_table))

if __name__ == "__main__":
    test()
