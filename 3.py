# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072

number = int(input("please type a number: "))
a = []
h = 0
for i in range(1, number+1):
    a.append((1+1/i)**i)
    h += float(a[i-1])
print(a)
print(round(h,3))

