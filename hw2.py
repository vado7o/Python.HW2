# Задача 1. Программа, которая принимает на вход вещественное число и показывает сумму его цифр.

# import os

# os.system('cls')
# input_digit: any
# count = 0

# while True:
#     input_str = input('Введите вещественное число: \n')
#     try:
#         input_digit = int(input_str)
#         for i in range(len(input_str)):
#             count += int(input_str[i])
#         print(f'\nСумма цифр введённого Вами числа равна = {count}')
#         break
#     except: 
#         try:
#             input_digit = float(input_str)
#             for i in range(len(input_str)):
#                 try:
#                     count += int(input_str[i])
#                 except:
#                     continue
#             print(f'\nСумма цифр введённого Вами числа равна = {count}')
#             break
#         except:
#             print('Неправильно введено число!')
#             continue

# *************************************************************************************************************

# Задача 2. Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# import os

# os.system('cls')
# input_int = 0

# while True:
#     try:
#         input_int = int(input('Введите целое число больше 0 : \n'))
#         if input_int < 1:
#             print('\nВы ввели число меньше 1!')
#             continue
#         break
#     except: 
#         print('\nНеправильно введено целое число!')

# collection = [1]
# for i in range(1, input_int):
#     collection.append(collection[i - 1] * (i + 1))
# print(f'\nНабор произведений чисел от 1 до {input_int} : {collection}')

# *************************************************************************************************************

# Задача 3. Список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# import os

# os.system('cls')

# while True:
#     try:
#         input_int = int(input('Введите целое число больше 0 : \n'))
#         if input_int < 1:
#             print('\nВы ввели число меньше 1!')
#             continue
#         break
#     except: 
#         print('\nНеправильно введено целое число!')

# array = dict()
# for i in range(input_int):
#     array[i + 1] = (1 + 1 / (i+1)) ** (i+1)

# print(f'Для n = {input_int}: {array}')

# ********************************************************************************************************

# Задача 4. Реализуйте алгоритм перемешивания списка.

# import os
# from random import shuffle

# os.system('cls')

# x = [[i] for i in range(21)]
# shuffle(x)
# print(x)