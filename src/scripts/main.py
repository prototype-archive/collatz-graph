import re
import numpy as np
from matplotlib import pyplot as plt
from pyscript.web import page
from pyscript import display

def calc_value(value):
    global cache
    if cache_size >= value:
        if not cache[value - 1]:
            cache[value - 1] = value // 2 if not value % 2 else value * 3 + 1
        value = cache[value - 1]
    else:
        value = value // 2 if not value % 2 else value * 3 + 1

    return int(value)


fig, ax = plt.subplots()
ax.set(xlabel='loop', ylabel='number')
ax.grid()

data_dict = {}
number_input = page["#number_input"][0]

cache_size = int(1e7)
cache = np.zeros(cache_size, dtype=np.uint64)

def get_array(value):
    number_list = []
    while True:
        number_list.append(value)
        if value == 1: break

        value = calc_value(value)

    return number_list

def make_graph(*args, **kwargs):
    global data_dict

    try:
        value = int(number_input.value)
    except ValueError as err:
        if len(args) > 0:
            value = int(args[0])
        else:
            return err

    if value < 2:
        return

    if value not in data_dict.keys():
        data = get_array(value)

        data_dict[value] = [max(data), len(data)]
        write_plot(data)

    page["#data_value"].innerText = "Max value: {}\n{} loops".format(*data_dict[value])

def write_plot(data):
    ax.plot(data)
    display(fig, target = "plot")

def number_update(*args, **kwargs):
    try:
        value = int(number_input.value)

        if value < 2:
            number_input.value = '2'
    except ValueError as err:
        if number_input.value != '': number_input.value = re.sub(r'[^0-9]', '', number_input.value)
        if number_input.value == '': number_input.value = '2'
