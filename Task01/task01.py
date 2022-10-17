# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:    
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = int(input('Введите число организации списка: '))
import random
number_list = []
i = 0
for i in range (0, n*2):
    el = random.randint(0, n)
    number_list.append(el)
    i += 1

print(number_list)

idx = 1
numbers_sum = 0
while idx <= len(number_list):
    numbers_sum = number_list[idx] + numbers_sum
    idx += 2
print(numbers_sum)