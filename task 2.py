# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

three_digit_number = int(input('Введите трёх значное число: '))
summa = 0
while three_digit_number > 0:
    x = three_digit_number % 10
    summa += x
    three_digit_number //= 10
else:
    print(f'Сумма чисел = {summa}')    

