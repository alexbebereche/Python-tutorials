class Dog:
    breed = "beagle"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"{self.name} is {self.age} years old"    

    def bark(self):
        return f"{self.name} barks"

dog = Dog("Spike", 5)
print(dog.describe())
print("He is a " + dog.breed)

dog2 = Dog("Spike", 5)
print(dog == dog2)

print(dog)