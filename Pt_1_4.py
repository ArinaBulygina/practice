while True:
    number = int(input("Введите число в диапазоне от 10 до 20: "))
    if number < 10:
        print("Число меньше требуемого диапазона, повторите попытку!")
    elif number > 20:
        print("Число больше требуемого диапазона, повторите попытку!")
    else:
        print("Спасибо")
        break
