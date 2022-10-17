# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> '101101'
# 3 -> '11'
# 2 -> '10'
# Примечание: Результат вернуть в виде строки. Не использовать функции преобразования типов: bin

inp_number = int(input('Введите число для конвертации:'))
b_number = []
b_el = ''

while inp_number > 0:
    b_el = inp_number % 2
    b_number.append(b_el)
    inp_number = inp_number // 2
b_number.reverse()

for i in b_number:
    print(i, end = "")
