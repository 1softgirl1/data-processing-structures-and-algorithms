def tribonacci(n):
    # Базовые случаи
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Рекурсивный случай: сумма трех предыдущих чисел
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

print(tribonacci(0))  # 0
print(tribonacci(1))  # 0
print(tribonacci(2))  # 1
print(tribonacci(3))
print(tribonacci(4))  # 2 (0+1+1)
print(tribonacci(5))  # 4 (1+1+2)
print(tribonacci(6))  # 7 (1+2+4)