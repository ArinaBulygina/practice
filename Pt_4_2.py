string = input("Введите строку: ")
palindromes = []
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        stroke = string[i:j]
        reversed_stroke = "".join(reversed(stroke))
        if stroke == reversed_stroke and len(stroke) > 1:
            palindromes.append(stroke)

print("Все палиндромы: ", palindromes)
