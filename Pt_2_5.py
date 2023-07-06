import random

win = defeat = consecutive_losses = 0
while consecutive_losses < 3:
    user = input('Орёл или Решка? (Орёл - 0, Решка - 1): ')
    if user not in '01':
        print('Конец игры')
        break
    computer = random.choice('01')
    if computer == user:
        print("Вы победили!")
        win += 1
        consecutive_losses = 0
    else:
        print("Вы проиграли")
        defeat += 1
        consecutive_losses += 1
    print(f'Побед: {win}\nПоражений: {defeat}\nПоражений подряд: {consecutive_losses}')
print('Лимит поражений подряд исчерпан. Конец игры')
