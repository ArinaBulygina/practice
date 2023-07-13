string = input("Введите слово: ")
dictionary = {}
x = 'aAeEiIоOuUyYаАяЯуУюЮоОеЕёЁэЭиИыЫ'
for i in string:
    if i != " ":
        if i in x:
            dictionary[i] = True
        else:
            dictionary[i] = False
print("Словарь: ", dictionary)
