string = input("Введите строку: ")
x = ""
for i in string:
    if i.isupper():
        x += i.lower()
    else:
        x += i.upper()
print("Полученная строка: ", x)
