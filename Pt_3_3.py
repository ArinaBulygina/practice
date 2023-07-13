number = int(input("Введите число: "))
(lambda x: print("Число чётное!") if x % 2 == 0 else print("Число нечетное"))(number)
