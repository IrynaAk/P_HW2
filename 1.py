# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input("please type a number: "))
st = str(number)
a = list(st)
h = 0
for i in range(len(a)):
    if a[i] == '.':
        continue
    h += int(a[i])
#print(a)
print(h)
