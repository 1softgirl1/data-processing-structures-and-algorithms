import random
import timeit

import matplotlib.pyplot as plt


# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Измерение времени
def measure_time(sort_func, data):
    stmt = lambda: sort_func(list(data))
    return timeit.timeit(stmt, number=1)


# Размеры массивов для тестов
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Результаты
selection_times_random = []
quick_times_random = []

selection_times_sorted = []
quick_times_sorted = []

selection_times_reverse = []
quick_times_reverse = []

for size in sizes:
    random_arr = [random.randint(0, 1000) for _ in range(size)]
    sorted_arr = list(range(size))
    reverse_arr = list(range(size, 0, -1))

    # Измеряем время
    t1 = measure_time(selection_sort, random_arr)
    t2 = measure_time(quick_sort, random_arr)
    selection_times_random.append(t1)
    quick_times_random.append(t2)

    t3 = measure_time(selection_sort, sorted_arr)
    t4 = measure_time(quick_sort, sorted_arr)
    selection_times_sorted.append(t3)
    quick_times_sorted.append(t4)

    t5 = measure_time(selection_sort, reverse_arr)
    t6 = measure_time(quick_sort, reverse_arr)
    selection_times_reverse.append(t5)
    quick_times_reverse.append(t6)

    print(f"Размер {size}: выборка {t1:.4f}с, быстрая {t2:.4f}с")

# Рисуем графики
plt.figure(figsize=(15, 5))

# График 1: Случайные числа
plt.subplot(1, 3, 1)
plt.plot(sizes, selection_times_random, 'ro-', label='Выбором')
plt.plot(sizes, quick_times_random, 'bo-', label='Быстрая')
plt.title('Случайные числа')
plt.xlabel('Размер')
plt.ylabel('Время (сек)')
plt.legend()

# График 2: Отсортированный
plt.subplot(1, 3, 2)
plt.plot(sizes, selection_times_sorted, 'ro-', label='Выбором')
plt.plot(sizes, quick_times_sorted, 'bo-', label='Быстрая')
plt.title('Отсортированный')
plt.xlabel('Размер')
plt.ylabel('Время (сек)')
plt.legend()

# График 3: Обратный порядок
plt.subplot(1, 3, 3)
plt.plot(sizes, selection_times_reverse, 'ro-', label='Выбором')
plt.plot(sizes, quick_times_reverse, 'bo-', label='Быстрая')
plt.title('Обратный порядок')
plt.xlabel('Размер')
plt.ylabel('Время (сек)')
plt.legend()
plt.show()