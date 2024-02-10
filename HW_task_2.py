# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions
import math


def reducing(numerator, denominator):
    numerator //= math.gcd(numerator, denominator)
    denominator //= math.gcd(numerator, denominator)
    return str(numerator) + '/' + str(denominator)


num_1 = list(map(int, input(
    "Введите 1-ю дробь с числителем и знаменателем в формате “a/b”: ").split('/')))
num_2 = list(map(int, input(
    "Введите 2-ю дробь с числителем и знаменателем в формате “a/b”: ").split('/')))

print("Сумма дробей равна", fractions.Fraction(num_1[0], num_1[1]) +
      fractions.Fraction(num_2[0], num_2[1]))
print("Произведение дробей равно", fractions.Fraction(num_1[0], num_1[1]) *
      fractions.Fraction(num_2[0], num_2[1]))
numerator = num_1[0] * num_2[1] + num_2[0] * num_1[1]
denominator = num_1[1] * num_2[1]

if numerator % denominator == 0:
    print("Сумма дробей равна", numerator // denominator)
else:
    print("Сумма дробей равна", reducing(numerator, denominator))
numerator = num_1[0] * num_2[0]
if numerator % denominator == 0:
    print("Произведение дробей равно", numerator // denominator)
else:
    print("Произведение дробей равно", reducing(numerator, denominator))
