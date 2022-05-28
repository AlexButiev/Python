#  Структуры с повторением
#  Алгоритмический тренажер

# # Напишите цикл w h i l e , который позволяет пользователю ввести число.
# # Число должно быть умножено на 1О, и результат присвоен переменной с
# # именем product. Цикл должен повторяться до тех пор, пока product меньше 100.
#
# product = 0         # Инициализируем аккумулирующую переменную
# while product < 100:
#     number = int(input('Введите число: ')) * 10
#     product += number
# print("Итого: ", product)

# # 2.
# # Напишите цикл w h i l e , который просит пользователя ввести два числа.
# # Числа должны быть сложены, и показана сумма. Цикл должен запрашивать у
# # пользователя, желает ли он выполнить операцию еще раз. Если да, то цикл
# # должен повториться, в противном случае он должен завершиться.
#
# repeat = "y"
#
# while repeat == 'y' or repeat == 'Y':
#     num_1 = float(input('Put first number: '))
#     num_2 = float(input('Put second number: '))
#     sum_numbers = num_1 + num_2
#     print('Sum is:', sum_numbers)
#     repeat = input('For repeat press "Y" '
#                    'or press any key: ' )

# # Напишите цикл for, который выводит приведенный ниже
# # ряд чисел: О, 10, 20, 30, 40, 50, ..., 1000
# for num in range(0,1001, 10):
#     print(num, end=', ')

# Напишите цикл, который просит пользователя ввести число.
# Цикл должен выполнить 1О итераций и вести учет
# нарастающего итога введенных чисел.

# sum = 0
# number = int(input('Put the number: '))
# for num in range(10):
#     sum += number
#     print(sum, end=', ')

# # Напишите цикл, который вычисляет сумму приведенного ниже числового ряда:
# # 1/30 + 2/ 29 + 3/ 28 + ... 30/1
#
# sum = 0
# numerator = 1
# denominator = 30
# for x in range(30):
#     action = numerator / denominator
#     numerator += 1
#     denominator -= 1
#     sum += action
# print(format(sum, '.2f'))

# # Напишите серию вложенных циклов, которые выводят 10 строк символов #.
# # В каждой строке должно быть 15 символов #.
#
# lines = 10
# symbols = 15
# for line in range(lines):
#     for symbol in range(symbols):
#         print('#', end='')
#     print()

# # Напишите программный код, который предлагает пользователю
# # ввести положительное ненулевое число и выполняет проверку
# # допустимости входного значения.
#
# number = float(input('Введи положительное, ненулевое число: '))
# while number <= 0:
#     print('Я же сказал - положительное ненулевое число!')
#     number = float(input('Для особо одарённых еще одна попытка: '))
# print('Молодец! Теперь ты будешь знать, что', number,
#       'является положительным и ненулевым числом')

# # Напишите программный код, который предлагает пользователю
# # ввести число в диапазоне от 1 до 100 и проверяет
# # допустимость введенного значения.
#
# number = int(input('введи число от 1 до 100: '))
# while number < 1 or number > 100:
#     print('Ошибка!')
#     number = int(input('введи число от 1 до 100: '))

# # Сборщик ошибок.
# #Сборщик ошибок собирает ошибки каждый день в течение пяти дней.
# # Напишите программу, которая ведет учет нарастающего итога ошибок, собранных в
# # течение пяти дней. Цикл должен запрашивать количество ошибок, собираемых в течение
# # каждого дня, и когда цикл завершается, программа должна вывести общее количество собранных ошибок.
#
# errors = 0
# days = 5
# for day in range(days):
#     print(day+1, 'День')
#     errorsForDay = int(input('Введите количество ошибок за день: '))
#     print('Количество ошибок за', day+1, 'день составило сумму: ', errorsForDay)
#     print('_______________________________')
#     errors += errorsForDay
# print('Общее количество собранных ошибок за', days, 'дней:', errors)

# # Сожженные калории.
# # Бег на беговой дорожке позволяет сжигать 4,2 калорий в минуту.
# # Напишите программу, которая применяет цикл для вывода количества калорий,
# # сожженных после 10, 15, 20, 25 и 30 минут бега.
#
# print('Сожжёные каллории')
# print('_______________')
# MIN_MIN = 10
# MAX_MIN = 31
# INCREMENTER = 5
# effectOfRun = 4.2
#
# print('10 min\t15\min\t20min\t25min\t30min')
# for min in range(MIN_MIN, MAX_MIN, INCREMENTER):
#      print(min * effectOfRun, end='\t')

# # Анализ бюджета.
# # Напишите программу, которая просит пользователя ввести сумму, выделенную им на
# # один месяц. Затем цикл должен предложить пользователю ввести суммы отдельных
# # статей его расходов за месяц и подсчитать их нарастающим итогом. По завершению
# # цикла программа должна вывести сэкономленную или перерасходованную сумму.
#
# print('Анализ бюджета')                                                 # Название программы
# print('_______________')
#
# sumOfStatesBudjet = 0
# budjet = float(input('Введите сумму на один месяц: '))                  # Запрос суммы бюджета
# numbersOfStates = int(input('Сколько статей расхода в этом месяце: '))  # Запрос количества статей расхода
# for state in range(numbersOfStates):                                    # Цикл
#     print('Введите сумму расходов. Статья', state + 1, end='')
#     stateOfBudjet = float(input(': '))
#     sumOfStatesBudjet += stateOfBudjet
# if sumOfStatesBudjet > budjet:
#     print('В этом месяце вы превысили сумму бюджета на $', sumOfStatesBudjet - budjet, sep='')
# elif sumOfStatesBudjet == budjet:
#     print('Вы ровно уложились в бюджет')
# else:
#     print('В этом месяце вам удалось сэкономить $', budjet - sumOfStatesBudjet, sep='')

# # Напишите программу, которая применяет вложенные циклы для рисования этого узора:
#
# # *******
# # ******
# # *****
# # ****
# # ***
# # **
# # *
#
# for line in range(7, 0, -1):
#     for sym in range(line):
#         print('*', end='')
#     print()
