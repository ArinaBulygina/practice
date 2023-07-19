string = input("Введите строку для кодировки: ")
a = 'abcdefghijklm'
b = 'nopqrstuvwxyz'
for i in range(len(string)):
    if string[i] in a:
        for j in range(len(a)):
            if string[i] == a[j]:
                string = string[:i] + b[j] + string[i + 1:]
    else:
        for k in range(len(b)):
            if string[i] == b[k]:
                string = string[:i] + a[k] + string[i + 1:]
print("Полученная строка: ", string)
