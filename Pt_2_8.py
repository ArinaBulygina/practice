import sys

n = float(input("Введите число: "))
for number in range(sys.maxsize):
    if number**2 > n:
        print("Первое число, квадрат которого больше заданного числа n:", number)
        break
