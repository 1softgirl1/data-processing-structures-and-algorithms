import matplotlib.pyplot as plt
import timeit

# функция возвращает список всех простых чисел от 1 до n включительно
# Вычислительная сложность алгоритма: O(n²)

def foo(n):
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1
        if divisors == 0:
            res.append(i)
    return res

n = [10, 100, 1000, 10000, 25000, 50000]
res = []
for i in n:
    res.append(timeit.timeit(lambda: foo(i), number=1))
plt.plot(n, res)
plt.show()

