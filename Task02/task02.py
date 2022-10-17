# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

n = int(input('Введите размер списка списка: '))
import random
number_list = []
i = 0
for i in range (0, n):
    el = random.randint(0, 10)
    number_list.append(el)
    i += 1
print(number_list)

idx = 0
mult = 1
numbers_mult = []
while idx < len(number_list)//2:
    mult = number_list[idx] * number_list[-(idx + 1)]
    numbers_mult.append(mult)
    idx += 1
print(numbers_mult)