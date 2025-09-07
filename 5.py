import timeit
import matplotlib.pyplot as plt
import random

def test_list_membership(n, element_to_find):
    lst = list(range(n))
    return element_to_find in lst

def test_set_membership(n, element_to_find):
    s = set(range(n))
    return element_to_find in s


sizes = [5, 10, 50, 100, 500, 1000, 10000, 100000]

list_times = []
set_times = []
element_to_find = random.randint(0, 10000)

for size in sizes:
    list_times.append(timeit.timeit(lambda:test_list_membership(size, element_to_find), number=1))
    set_times.append(timeit.timeit(lambda:test_set_membership(size, element_to_find), number=1))


plt.plot(sizes, list_times, color = 'blue')
plt.plot(sizes, set_times, color = 'red')
plt.show()
