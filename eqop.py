a = 10
b = 10

# python has some integer values stored into an array already: -5 to 256
"""
if the values are the same, for ex: 3000, not True in idle
"""
print(a == b)
print(a is b)

print(id(a))
print(id(b))

a = 5
b = 0
b += 5

print(a == b)
print(a is b)

print(id(a))
print(id(b))

c = 3000
d = 0
d += 3000
# d = 3000

print(c == d)
print(c is d)

print(id(c))
print(id(d))

print("-------lists")
a = [1,2,3,4,5]
b = [1,2,3,4,5]

print(a == b)
print(a is b)
print("-------strings")

a = "asd"
b = "asd"
print(a == b)
print(a is b)

a = "asd"
b = "as"
b += "d"

print(a == b)
print(a is b)