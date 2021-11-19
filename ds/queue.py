from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)