import math
import statistics
from functools import reduce


def area(r):
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 12]

# direct

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

# better: map(function, data)
map(area, radii)  # map object, iterator
list(map(area, radii))  # list

temps = [("Berlin", 20), ("Bucharest", 36), ("Tokyo", 25)]
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
print(list(map(c_to_f, temps)))

# filter
data = [1.3, 2.5, 0.4, 3.1, -.1, 3.4]
avg = statistics.mean(data)
print(avg)

filter(lambda  x: x > avg, data)  # filter object
print(list(filter(lambda  x: x > avg, data)))

# remove missing data
countries_sa = ["", "Arg", "Br", "Ch", "Co", ""]

print(list(countries_sa))
print(list(filter(None, countries_sa)))

# careful: 0 False value, but prob don't want to filter it

# reduce, no longer built-in

data = [1.3, 2.5, 0.4, 3.1, 6, 3.4]
# multiplier = lambda x, y: x * y


def multiply(x, y):
    return x * y


print(reduce(multiply, data))  # better than a for loop

