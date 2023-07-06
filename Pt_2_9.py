number = input("Введите число: ")
number = " ".join(number).split()
max = -1
for i in range(len(number)):
    if int(number[i]) > max:
        max = int(number[i])
        index = i+1
print("Порядковый номер максимальной цифры считая от начала числа: ", index)
index = 0
for i in range(len(number)-1, -1, -1):
    print(i)
    if int(number[i]) == max:
        index = len(number) - i
print("Порядковый номер максимальной цифры считая от конца числа: ", index)
