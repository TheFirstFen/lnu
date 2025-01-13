def compute_x_trees(n):
    return n ** (n-2)


n = 6
print(f"Total # of complete spanning trees for n={n}: ", compute_x_trees(n))
