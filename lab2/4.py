import timeit
import functools

from matplotlib import pyplot as plt


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def fib_with_lucas(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    i = n // 2
    j = n - i
    Fi = fib_with_lucas(i)
    Fj = fib_with_lucas(j)
    Li = lucas_with_fib(i)
    Lj = lucas_with_fib(j)

    return (Fi * Lj + Fj * Li) // 2


def lucas_with_fib(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n + 1)

def measure_performance():
    n = 35
    n_values = list(range(5, n + 1, 2))

    fib_times = []
    luc_times = []
    fib_with_lucas_times = []

    for n in n_values:
        fib_time = timeit.timeit(functools.partial(fibonacci, n), number=1)
        fib_with_lucas_time = timeit.timeit(functools.partial(fib_with_lucas, n), number=1)
        luc_time = timeit.timeit(functools.partial(lucas, n), number=1)

        fib_times.append(fib_time)
        fib_with_lucas_times.append(fib_with_lucas_time)
        luc_times.append(luc_time)

        fib_result = fibonacci(n)
        fib_with_lucas_result = fib_with_lucas(n)
        luc_result = lucas(n)

        if fib_result != fib_with_lucas_result:
            print(f"Результаты не совпадают для n = {n} "
                  f"(fib={fib_result}, fib_with_lucas={fib_with_lucas_result})")


        print(f"F({n}) = {fib_result}")
        print(f"Время вычисления Fibonacci({n}): {fib_time:.6f} секунд")
        print(f"Время вычисления Fibonacc через Lucas({n}): {fib_with_lucas_time:.6f} секунд")
        print(f"\nL({n}) = {luc_result}")
        print(f"Время вычисления Lucas({n}): {luc_time:.6f} секунд")



    plt.figure(figsize=(12, 6))
    plt.plot(n_values, fib_times, 'bo-', label='Стандартный Фибоначчи', linewidth=2)
    plt.plot(n_values, fib_with_lucas_times, 'ro-', label='Фибоначчи через Люка', linewidth=2)
    plt.xlabel('n')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение производительности алгоритмов Фибоначчи')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


measure_performance()