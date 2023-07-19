a, b = int(input("Введите начало диапазона: ")), int(input("Введите конец диапазона: "))
sum = 0
for i in range(a, b + 1):
    sum += i
print("Сумма чисел в заданном диапазоне: ", sum)
