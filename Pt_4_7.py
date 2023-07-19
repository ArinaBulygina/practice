import itertools

s = input("Введите строку: ")
permutations = itertools.permutations(s)
k = 0
for per in permutations:
    k += 1
print("Количество перестановок: ", k)
