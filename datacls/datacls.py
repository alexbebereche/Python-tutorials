from dataclasses import dataclass, field

"""no need to provide constructor, repr, eq; just the fields"""

@dataclass(order=True)  # frozen=True for immutable, unsafe_hash=True -> mutable
class Investor:
    sort_index: float = field(init=False, repr=False) # will determine the order
    name: str
    age: int
    cash: float = field(repr=False, compare=False, default=0.0)

    # add another field
    # favSport: str

    # can still override fcts
    # def __repr__(self):
    #     return "hi"

    def __post_init__(self):
        self.sort_index = self.cash

i1 = Investor("Alex", 22, 1000)
i2 = Investor("Eugen", 21)
i3= Investor("Alex", 22, 900)
i4= Investor("Mihai", 22, 30000)


print(i1)
print(i1 == i2)
print(i1 == i3)

print(i1 > i3)

myList = [i1, i2, i3, i4]
print(sorted(myList))