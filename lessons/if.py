# # Именнованная константа HIGHSCORE содержит значение, которое считается высоким баллом.
# HIGH_SCORE = 95
#
# # Получить три оценки за контрольные работы.
# test1 = int(input("Введите оценку 1: "))
# test2 = int(input("Введите оценку 2: "))
# test3 = int(input("Введите оценку 3: "))
#
# # Расчитать средний балл
# avarage = (test1 + test2 + test3) / 3
#
# # Напечатать средний балл
# print("Средний балл составляет: ", avarage)
#
# # Если средний балл высокий - поздравить ученика
# if avarage >= 95:
#     print("Поздравляем!\nОтличный средний балл!")

# Эта программа получает от пользователя числовую оценку
# и показывает буквенный уровень знаний согласно этой оценке.

# Именованные константы, представляющие пороги уровней.
# A_SCORE = 90
# B_SCORE = 80
# C_SCORE = 70
# D_SCORE = 60

# Получить от пользователя оценку за контрольную работу.
# score = int(input("Введите свою оценку: "))
#
# if score >= A_SCORE:
#     print("Ваш уровень - А")
# else:
#     if score >= B_SCORE:
#         print("Ваш уровень - B")
#     else:
#         if score >= C_SCORE:
#             print("Ваш уровень - C")
#         else:
#             if score >= D_SCORE:
#                 print("Ваш уровень - D")
#             else:
#                 print("Ваш уровень - F")

# То же самое но if-elif-else:
# if score >= A_SCORE:
#     print("Ваш уровень - А")
# elif score >= B_SCORE:
#     print("Ваш уровень - B")
# elif score>= C_SCORE:
#     print("Ваш уровень - C")
# elif score >= D_SCORE:
#     print("Ваш уровень - D")
# else:
#     print("Ваш уровень - F")

# Напишите инструкцию if, которая присваивает значение 20 переменной у и значение 40
# переменной z, если переменная х больше 100.

# x = 120
# if x > 100:
#     y = 20
#     z = 40
#     print("y =", y)
#     print("z =", z)
# else:
#     print("x <= 100")

# Напишите вложенные структуры принятия решения,
# которые выполняют следующее: если amountl
# больше 10 и amount2 меньше 100, то показать
# большее значение из двух пе­ ременных
# amountl и amount2.

# amount1 = 45
# amount2 = 89
# if amount1 > 10 and amount2 < 100:
#     if amount1 > amount2:
#         print(amount1)
#     else:
#         print(amount2)
# else:
#     print("amount2 and amount 1 вне диапозона")

# Напишите инструкцию i f - e l s e , которая выводит
# сообщение 'Скорость нормальная', если переменная
# s p e e d находится в диапазоне от 24 до 56.
# Если значение переменной s p e e d лежит вне
# этого диапазона, то показать 'Скорость аварийная'.

# speed = int(input("put your speed: "))
# if speed >= 24 and speed <= 56:
#     print("Your speed is normal")
# else:
#     print("Your speed is dangerous")

# Напишите инструкцию if-else, которая определяет,
# находится ли переменная points вне диапазона
# от 9 до 51. Если значение переменной лежит вне
# этого диапазона, то она должна вывести сообщение
# ' Недопустимые точки' . В противном случае она
# должна показать сообщение 'Допустимые точки' .

# points = int(input("value of points: "))
# if points >= 9 and points <= 51:
#     print("Допустимые точки")
# else:
#     print("Недопустимые точки")

# День недели. Напишите программу, которая
# запрашивает у пользователя число в диапазоне
# от 1 до 7. Эта программа должна показать
# соответствующий день недели, где l - понедельник,
# 2 - вторник, 3 - среда, 4 - четверг, 5 - пятница,
# 6 - суббота и 7 - воскресенье. Программа должна
# вывести сообщение об ошибке, если пользователь
# вводит номер, который находится вне диапазона от 1 до 7.

# day = int(input("Введите день недели: "))
# if day < 1 or day > 7:
#     print("Вне диапозона")
# elif day == 1:
#     print("Mon")
# elif day == 2:
#     print("Tue")
# elif day == 3:
#     print("Wen")
# elif day == 4:
#     print("Th")
# elif day == 5:
#     print("Fr")
# elif day == 6:
#     print("Sat")
# else:
#     print("San")

# Площади прямоугольников. Площадь прямоугольника- это
# произведение его длины на его ширину. Напишите
# программу, которая запрашивает длину и ширину
# двух прямоугольников. Программа должна выводить
# пользователю сообщение о том, площадь какого
# прямоугольника больше, либо сообщать, что они одинаковы.

# lenght1 = int(input("Длина 1: "))
# width1 = int(input("Ширина 1: "))
# lenght2 = int(input("Длина 2: "))
# width2 = int(input("Ширина 2: "))
#
# square1 = lenght1 * width1
# square2 = lenght2 * width2
# print("Square1 =", square1)
# print("Square2 =", square2)
#
# if square1 > square2:
#     print("Square1 > Square2")
# elif square1 < square2:
#     print("Square2 > Square1")
# else:
#     print("Square1 = Square2")

# Напишите программу, которая вычисляет и
# показывает индекс массы тела (ИМТ) человека.
# ИМТ часто используется для определения,
# весит ли человек больше или меньше нормы
# для своего. ИМТ человека рассчитывают по формуле:
# ИМТ= масса / рост
# где масса измеряется в килограммах,
# а рост - в метрах. Программа должна
# попросить пользователя ввести массу
# и рост и затем показать ИМТ пользователя.
# Программа также должна вывести сообщение,
# указывающее, имеет ли человек оптимальную,
# недостаточную или избыточную массу.
# Масса человека считается оптимальной,
# если его ИМТ находится между 18.5 и 25.
# Если ИМТ меньше 18.5, то считается, что
# человек весит ниже нормы. Если значение И
# МТ больше 25, то считается, что человек
# весит больше нормы.

# height = float(input("Введите свой рост в метрах: "))
# weight = int(input("Введите свой вес в кг: "))
#
# imt = weight / height ** 2
# print()
# print("Ваш ИМТ =", format(imt, '.2f'))
# if imt >= 18.5 and imt <=25:
#     print("Вес оптимален")
# elif imt < 18.5:
#     print("Вес ниже нормы")
# else:
#     print("Вес больше нормы")

# Калькулятор времени. Напишите программу, которая просит пользователя ввести количество секунд
# и работает следующим образом. В минуте 60 секунд. Если число введенных пользователем секунд
# больше или равно 60, то программа должна преобразовать число секунд в минуты и секунды.
# В часе 3 600 секунд. Если число введенных пользователем секунд больше или равно 3 600,
# то программа должна преобразовать число секунд в часы, минуты и секунды. В дне 86 400 секунд.
# Если число введенных пользователем секунд больше или равно 86 400, то программа должна
# преобразовать число секунд в дни, часы, минуты и секунды.

# seconds = int(input("Введите количество секунд: "))
# if seconds >= 60 and seconds <3600:
#     minutes = seconds // 60 % 60
#     seconds = seconds % 60
#     print('Минут:', minutes)
# elif seconds >= 3600 and seconds < 86400:
#     hours = seconds // 3600
#     minutes = (seconds // 60) % 60
#     seconds = seconds % 60
#     print('Часов:', hours)
#     print('Минут:', minutes)
# elif seconds >= 86400:
#     days = seconds // 86400
#     hours = seconds // 3600
#     minutes = (seconds // 60) % 60
#     seconds = seconds % 60
#     print('Дней:', days)
#     print('Часов:', hours)
#     print('Минут:', minutes)
# print('Cекунд:', seconds)
