from functools import reduce
from itertools import combinations

number = int(input("Введите число: "))
numbers = [x for x in range(1, 15)]
unique_comb = []

for r in range(1, len(numbers) + 1):
    combinations_r = combinations(numbers, r)
    unique_comb.extend(combinations_r)
sum_comb = []
for i in unique_comb:
    sum = reduce(lambda x, y: x + y, i)
    if sum == number:
        sum_comb.append(i)

print(f"Комбинации: {sum_comb} из списка: {numbers}")
