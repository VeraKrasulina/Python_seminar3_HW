# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibon_pos(n):
    if n < 3:
        return 1
    return fibon_pos(n - 1) + fibon_pos(n - 2)

def fibon_neg(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    return fibon_neg(n + 2) - fibon_neg(n + 1)

inp_number = int(input('Введите число: '))
if inp_number > 0: inp_number = - inp_number
tmp = - inp_number
fibonacci = []
f_el = ''

while inp_number < 0:
    f_el = fibon_neg(inp_number)
    fibonacci.append(f_el)
    inp_number += 1
fibonacci.append(0)

fibonacci_tmp = []
while tmp > 0:
    f_el = fibon_pos(tmp)
    fibonacci_tmp.append(f_el)
    tmp -= 1
fibonacci_tmp.reverse()

fibonacci += fibonacci_tmp
print(fibonacci)