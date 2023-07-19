import random

colors = "Красный Синий Жёлтый Зелёный Чёрный"
print(colors)
string = colors.split()

color = input("Введите цвет из списка, который по вашему мнению выбрала программа: ")
index_pc_color = int(random.choice("01234"))
while True:
    if color != string[index_pc_color]:
        if string[index_pc_color] == "Красный":
            print("Неправильно! \nПодсказка: Такого цвета пламя")
        if string[index_pc_color] == "Синий":
            print("Неправильно! \nПодсказка: Такого цвета море")
        if string[index_pc_color] == "Жёлтый":
            print("Неправильно! \nПодсказка: Такого цвета солнце")
        if string[index_pc_color] == "Зелёный":
            print("Неправильно! \nПодсказка: Такого цвета трава")
        if string[index_pc_color] == "Чёрный":
            print("Неправильно! \nПодсказка: Такого цвета тень")
    else:
        print("Отлично!")
        break
    print(colors)
    color = (input("Попробуйте снова, введите цвет: "))
