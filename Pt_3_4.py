list = [int(input("Введите число списка: ")) for i in range(3)]
print(f"Исходный список: {list}")
new_list = [i ** 2 for i in list]
print(f"Новый список: {new_list}")
