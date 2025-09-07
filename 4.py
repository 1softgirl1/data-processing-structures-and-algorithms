import timeit
import matplotlib.pyplot as plt
import random

def test_list_deletion(n):
    lst = list(range(n))
    index = random.randint(0, n - 1)
    del lst[index]
    return lst


def test_dict_deletion(n):
    dct = {i: f"value_{i}" for i in range(n)}
    key = random.randint(0, n - 1)
    del dct[key]
    return dct

sizes = [5, 10, 50, 100, 500, 1000]

list_times = []
dict_times = []

for size in sizes:
    list_times.append(timeit.timeit(lambda:test_list_deletion(size), number=1))
    dict_times.append(timeit.timeit(lambda:test_dict_deletion(size), number=1))


plt.plot(sizes, list_times, color = 'blue')
plt.plot(sizes, dict_times, color = 'red')
plt.show()

