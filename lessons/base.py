# print("_______________________________________________________")
# topSpeed = 160
# distance = 300
# # показать значения на которые ссылаются переменные
# print("Предельная скорость составляет:")
# print(topSpeed)
# print("Пройденное расстояние составляет:")
# print(distance)
# print("_______________________________________________________")
# # Эта программа показывает повторное присвоение значения переменной.
# # Присвоить значение переменной rouЬles.
# roubles = 12.75
# print('У меня на счете', roubles, 'рублей.')
# # Повторно присвоить значение переменной rouЫes, 7 # чтобы она ссылалась на другое значение.
# roubles = 990.95
# print('А теперь там', roubles, 'рублей!')
# print("_______________________________________________________")
# # Создать переменные, которые ссылаются на два строковых значения.
# firstName = 'Кэтрин'
# lastName = 'Марино'
# # Показать значения, на которые эти переменные ссылаются.
# print(firstName, lastName)
# print("_______________________________________________________")

# originalPrice = float(input("Введите исходную цену товара: "))
# discount = originalPrice * 0.2                                  # вычисляем скидку 20%
# sale_price = originalPrice - discount
# print("Отпускная цена составляет: ", sale_price)

# # Получить от пользователя количество секунд
# totalSeconds = int(input("Введите количество секунд: "))
# # получить количество часов
# hours = totalSeconds // 3600
# # Получить оставшееся количество минут
# minutes = (totalSeconds // 60) % 60
# # Получить оставшееся количество секунд
# seconds = totalSeconds % 60
# # Показать результат
# print("Вот время в часах, минутах и секундах: ")
# print("Часы: ", hours)
# print("Минуты: ", minutes)
# print("секунды: ", seconds)

# # Get first user's name
# firstName = input("What's your name: ")
# # Get second user's name
# secondName = input("What's your second name: ")
# # Show hello list
# print("Hello,", firstName, secondName)
#
# # Чтение чисел при помощи функции input (из строки в число)
# stringValue = input("Сколько часов Вы отработали? ")
# hours = int(stringValue)
# # It's the same:
# hours = float(input("Сколько часов Вы отработали? "))
# print(type(hours))

# firstName = input("Как Вас зовут? ")
# age = int(input("Сколько Вам лет? "))
# income = float(input("Какой у Вас доход? "))
# print("Вот данные, которые Вы ввели:")
# print("Имя:", firstName)
# print("Ваш возраст:", age)
# print("Ваш доход:", income)

# Вам нужно, чтобы пользователь программы ввел объем продаж за неделю.
# Напишите инструкцию, которая предлагает пользователю
# ввести эти данные и присваивает их переменной.

# salesVolume = float(input("введите объем продаж: "))
# print("Объем продаж = ", salesVolume)

# salary = float(input("your salary: "))
# bonus = float(input("your bonus: "))
# pay = salary + bonus
# print("Ваш доход: ", pay)

# # Подавление концевого символа новой строки в функции print  (end='')
# print('One', 'two', 'three', end=' ')
# print('four', 'five', 'six', end=' ')
# print('seven', 'eight', 'nine', end=' ')
# print('ten')

# Задание символа-разделителя значений
# Если потребуется, чтобы между значениями
# печатался пробел, то в функцию print можно передать аргумент sep="":
# print("one", "two", "three", sep="~~~")

# Экранированные символы
# \n Переводит позицию печати на следующую строку
# \t Переводит позицию печати на следующую горизонтальную позицию табуляции
# \' Печатает одинарную кавычку
# \" Печатает двойную кавычку
# \\ Печатает обратную косую черту
# print("one\ntwo\nthree")
# print("ont\ttwo\tthree")
# print("Домашнее задание на завтра - прочитать \"Гамлета\".")
#
# # Конкатенация
# print('Этo ' + 'один строковый литерал.')
# # полезен при разбиение строкового литерала
# print("Введите объем " +
#       "продаж за каждый день и " +
#       "нажмите Enter")

# Форматирование чисел
# Эта программа демонстрирует, как ЧИСЛО
# с плавающей точкой выводится без форматирования.
# amountDue = 5000.0
# monthlyPayment = amountDue / 12.0
# print('Ежемесячный платеж составляет:', format(monthlyPayment, '.2f'))

# Эта программа демонстрирует как число с плавающей точкой
# может быть отформатировано качестве валюты
# monthlyPay = 30000.0
# annualPay = monthlyPay * 12
# print('Baшa годовая заработная плата составляет $' ,
#       format(annualPay, ',.2f'), sep="")

# В компании было подсчитано, что ее ежегодная прибыль,
# как правило, составляет 23% от общего объема продаж.
# Напишите программу, которая просит пользователя ввести
# плановую сумму общего объема продаж и затем показывает
# прибыль, которая будет получена от этой суммы.
# Подсказка: для представления 23% используйте значение 0.23.

# planValue = float(input("Введите плановую сумму общего  объема продаж: "))
# profit = planValue * 0.23
# print("Ваш доход составит: ", format(profit, ',.2f'), "рублей")

# Покупатель приобретает в магазине пять товаров.
# Напишите программу, которая запрашивает цену
# каждого товара и затем выводит накопленную стоимость
# приобретаемых товаров, сумму налога с продаж и итоговую сумму.
# Допустим, что налог с продаж составляет 7%.

# TAX = 0.07
# product1 = float(input("Введите стоимость первого товара: "))
# product2 = float(input("Введите стоимость второго товара: "))
# product3 = float(input("Введите стоимость третьего товара: "))
# product4 = float(input("Введите стоимость четвертого товара: "))
# product5 = float(input("Введите стоимость пятого товара: "))
# SumOfProducts = product1 + product2 + product3 + product4 + product5
# productTax = SumOfProducts * TAX
# totalSum = SumOfProducts + productTax
# print("Стоимость товаров составляет: ", format(SumOfProducts, ',.2f'), "руб.")
# print("Сумма налога с продаж: ", format(productTax, ',.2f'), "руб.")
# print("Итоговая сумма за товары: ", format(totalSum, ',.2f'), "руб.")

# Программа, которая преобразует показания температуры по шкале Цельсия в температуру по шкале Фаренгейта
# temperature_c = float(input("Введите температуру по шкале Цельсия: "))
# temperature_f = 9 / 5 * temperature_c + 35
# print("Данная температура по Фаренгейту будет равна: ", format(temperature_f, '.2f'), "градусов")


# Рецепт булочек предусматривает ингредиенты:
# 1.5 стакана сахара;
# 1 стакан масла;
# 2.75 стакана муки.
# С таким количеством ингредиентов этот рецепт позволяет приготовить 48 булочек.
# Напишите программу, которая запрашивает у пользователя, сколько булочек он хочет
# приготовить, и затем показывает число стаканов каждого ингредиента,
# необходимого для заданного количества булочек.

# roll = int(input("Сколько булочек Вы хотите приготовить: "))
# sugar = 1.5 / 48 * roll
# oil = 1 / 48 * roll
# flour = 2.75 / 48 * roll
# print("Для приготовления", roll, "булочек потребуется:")
# print(format(sugar, '.2f'), "стакана сахара")
# print(format(oil, '.2f'), "стакана масла")
# print(format(flour, '.2f'), "стакана муки")

