from functools import lru_cache


@lru_cache(maxsize=1000)  # max is 120 implicitly
def fibonacci(n):
    # validation
    if type(n) != int:
        raise TypeError("must be pos int")
    if n < 1:
        raise ValueError("must be pos int")

    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1, 501):
    print(i, ":", fibonacci(i))

# fibonacci("one")

for i in range(1, 51):
    print(fibonacci(i+1) / fibonacci(i))  # golden ratio
