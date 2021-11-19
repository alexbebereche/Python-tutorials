from itertools import chain

numbers = chain([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(next(numbers))
print(next(numbers))
print(next(numbers))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(chain(*matrix)))
print(type(matrix))