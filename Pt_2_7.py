sum = 0
while True:
    number = int(input("Введите число: "))
    if number < 0:
        sum += number
    else:
        print("Вы ввели неотрицательное число. Полученная сумма: ", sum)
        break
