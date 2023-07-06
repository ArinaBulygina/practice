number = input("Введите число: ")
string = " ".join(number).split()
sum = 0
for i in range(len(string)):
    sum += int(string[i]) ** len(string)
if sum == int(number):
    print("Это число Армстронга!")
else:
    print("Это НЕ число Армстронга")
