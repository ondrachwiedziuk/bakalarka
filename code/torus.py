from quandle import load_quandles, print_quandle
from itertools import product

def color_torus_knot(strands, twists, init_colored_strands, cayley):
    if twists == 0:
        return init_colored_strands
    else:
        colored_strands = [0 for i in range(strands)]
        for i in range(strands):
            if i == 0:
                colored_strands[-1] = init_colored_strands[i]
            else:
                colored_strands[i - 1] = cayley[init_colored_strands[0]][init_colored_strands[i]]

        return color_torus_knot(strands, twists-1, colored_strands, cayley)

def valid_coloring(strands, twists, init_colored_strands, cayley):
    colored_strands = color_torus_knot(strands, twists, init_colored_strands, cayley)
    return colored_strands == init_colored_strands


def coloring_torus_invariant(order, strands, twists):
    quandles = load_quandles(order)
    for q in quandles:
        for permutation in product(range(order), repeat=strands):
            if valid_coloring(strands, twists, list(permutation), q):
                if len(set(permutation)) == 1:
                    continue
                print_quandle(q)
                break

def main():
    order = 5
    strands = 2
    twists = 3
    print(f"Coloring torus with {strands} strands and {twists} twists using quandles of order {order}")
    coloring_torus_invariant(order, strands, twists)

if __name__ == "__main__":
    main()
