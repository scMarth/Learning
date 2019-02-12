import itertools

p = [1, 2, 3, 4, 5]
q = [6, 7, 8, 9, 10]

# cartesian product
print("Cartesian Product:")
for obj in itertools.product(p, q):
    print obj
print("")

# permutations
#    r-length tuples, all possible orderings, no repeated elements
print("Permutations:")
r = 3
p = [1, 2, 3]
for permutation in itertools.permutations(p, r):
    print permutation
print("")

# combinations
#    r-length tuples, in sorted order, no repeated elements
print("Combinations (no repeated elements):")
r = 3
p = [1, 2, 3]
for combination in itertools.combinations(p, r):
    print combination
print("")

# combinations
#    r-length tuples, in sorted order, with repeated elements
print("Combinations (with repeated elements):")
r = 3
p = [1, 2, 3]
for combination in itertools.combinations_with_replacement(p, r):
    print combination