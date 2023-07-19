string = (input("Введите строку: "))
dictionary = {i: string.count(i) for i in string if i.isalpha()}
print(dictionary)
