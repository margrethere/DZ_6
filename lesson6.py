# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Было
# numbers = [2, 3, 5, 9, 3]
# print (numbers[1::2])
# print (sum (numbers[1::2])) 


# Стало
# n = range(0, 10)
# print(sum(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 1, enumerate(n)))))


#ДЗ_2, №1
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Было
#float_num = input('input float number: ')
#print(type(float_num))
#sum = 0
#for i in float_num:
#    if i != '.':
#         sum += int(i)
#print(sum)

# Стало
# from functools import reduce

# n = input("Введите вещественное число: ").replace(',', '')
# m = list(map(int, n))
# print(f'Сумма цифр числа равна', reduce(lambda x, y: x + int(y), m))

#ДЗ_2, №2
#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки.

#Было
#from msilib import sequence

#n = int(input('Введите число: ')) 

#def get_squerence(n):
#    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

#nums = get_squerence(n)
#print(nums)
#print(round(sum(nums), 5))

#Стало
# n = int(input('Введите число N:\t'))
# fc = lambda x: (1 + 1 / x) ** x
# numbers = [fc(x) for x in range (1, n + 1)]
# print(round(sum(numbers), 3))


#ДЗ_2, №3
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Было
#n = int(input('input N: '))
#factorial = 1
#for i in range(1, n+1):
#    factorial *= i
#    print(factorial, end=' ')

#Стало

# def faktorial():

#     factorial = lambda f : f * factorial(f-1) if f > 0 else 1
#     print("Факториал заданного числа равен:", factorial(int(input('Введите число N:\t'))))

# faktorial()