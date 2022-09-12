# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

number = int(input("please type a number: "))
a = list(range(-number, number+1))
print(a)

number2 = int(input("please type a number: "))
number3 = int(input("please type a number: "))

res = int(a[number2])*int(a[number3])
print(res)
