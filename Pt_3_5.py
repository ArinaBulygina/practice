def check_not_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


list = [int(input("Введите число списка: ")) for n in range(5)]
print(f"Исходный список: {list}")
new_list = [n for n in list if check_not_simple(n)]
print(f"Новый список: {new_list}")
