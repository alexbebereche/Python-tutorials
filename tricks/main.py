# zip
names = list(zip(('Mrs', 'Mr'), ['Anna', 'Jack']))
print(names)

# reverse
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

# count
from collections import Counter
numbers = [1, 1, 1, 2, 1, 4, 4, 4, 3, 6]
c = Counter(numbers)
print(c)

username = "user"
host = "mail.com"
print(username, host,sep="@")

# swap dict
mydict= {1: 11, 2: 22, 3: 33}
mydict = {i: j for j, i in mydict.items()}
print(mydict)

# enumerate
s = "Python"
e = enumerate(s)
print(list(e))