from statistics import StatisticsError, mean
import statistics
from math import fsum

print(mean([2, 3, 4, 2, 3, 6, 4, 2]))

try:
    print(mean([]))
except statistics.StatisticsError:
    print("should have at least one data point")

# difference between sum and fsum
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

print(sum([0.1, 0.2]))
print(fsum([0.1, 0.2]))

print(f"{0.1:.28f}")
print(f"{0.2:.28f}")