import numpy as np
from matplotlib import pyplot as plt

x = lambda x: x * 3 + 1 if x % 2 else x / 2

fig, ax = plt.subplots()
ax.set(xlabel='loop', ylabel='number')

number_input = Element("number_input")
def make_graph(*args, **kwargs):
    number_list = []
    value = int(number_input.element.value)
    while True:
        number_list.append(int(value))
        if value == 1: break
        value = x(value)

    data = np.array(number_list, dtype=np.int64)

    ax.plot(data)
    ax.grid()
    fig
