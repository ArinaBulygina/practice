from functools import reduce

number = int(input("Введите заданное число: "))
print(0)
list = [0, 1]
while list[1] <= number:
    print(list[1])
    x = reduce(lambda z, y: z + y, list)
    list[0] = list[1]
    list[1] = x
