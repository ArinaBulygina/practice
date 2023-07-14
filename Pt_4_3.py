def check_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a, b = int(input("Введите начало диапазона: ")), int(input("Введите конец диапазона: "))
simple_numbers = []
for i in range(a, b+1):
    if check_simple(i):
        simple_numbers.append(i)
print("Все простые числа: ", *simple_numbers)
