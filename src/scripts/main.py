import numpy as np
from matplotlib import pyplot as plt

x = lambda x: x * 3 + 1 if x % 2 else x / 2

li = []
value = 837799
while True:
    li.append(int(value))
    if value == 1: break
    value = x(value)

data = np.array(li, dtype=np.int64)

fig, ax = plt.subplots()

ax.plot(data)
ax.set(xlabel='loop', ylabel='number')
ax.grid()

fig