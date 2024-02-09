# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

BASE = 16
remains = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

num = int(input('Введите целое число: '))
print(f"{num}(10) = {hex(num)}(16)")
res = ''
print(f"{num}(10) =", end='')
while num > 0:
    if num % BASE < 10:
        res = str(num % BASE) + res
    else:
        res = remains[num % BASE] + res
    num = num // BASE
print(f" {res}(16)")
