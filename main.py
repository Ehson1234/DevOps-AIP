import itertools


def f(x, y, z):
    return ((x or z) and (x != y)) ^ (y and (y or z))


combinations = list(itertools.product([0, 1], repeat=3))  # x, y, z
results = []


for x, y, z in combinations:
    results.append(f(x, y, z))

result_str = ''.join(map(str, results))
print(result_str)