numbers = (input("Первое число: ") + " " + input("Второе число: ") + " " + input("Третье число: "))
numbers = numbers.split()
numbers.sort(reverse=True)
print("Наибольшее число:", numbers[0], "Числа, отсортированные по убыванию ", " ".join(numbers))
