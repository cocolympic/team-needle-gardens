import itertools

colors = ["red", "blue"]
sizes = ["S", "M", "L"]
for item in itertools.product(colors, sizes):
    print(item)
