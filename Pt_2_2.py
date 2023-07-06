list = []
for i in range(4):
    list.append(input("Введите название телеканала: "))
print("Исходный список телеканалов: ")
for i in list:
    print(i)
channel, index = input("Введите название нового телеканала: "), int(input("Введите позицию нового телеканала: "))
list.insert(index, channel)
print("Новый список телеканалов: ")
for i in list:
    print(i)
