# # Эта программа показывает случайное число из диапозона от 1 до 10
#
# import random
#
#
# def main():
#     number = random.randint(1, 100)
#     print('Random number is ', number)
#
#
# main()

# Программа со случайным числом и функцией for

# def main():
#     for count in range(5):
#         print(random.randint(1, 100))
# #
# #
# main()

# Если требуется просто показать случайное число, то нет необходимости присваивать случайное число переменной.
# Можно отправить значение, возвращаемое из функции модуля random, непосредственно в функцию print:

# print(random.randint(1, 100))


# # Эта программа бросает кубики
#
# import random
#
# MIN_COUNT = 1
# MAX_COUNT = 6
#
# def main():
#     again = 'д'
#
#     while again == 'д' or again == 'Д':
#         print('Бросаем кубики...')
#         print(random.randint(MIN_COUNT, MAX_COUNT))
#         print(random.randint(MIN_COUNT, MAX_COUNT))
#         again = input('Кинуть кубики еще раз - нажмите "д": ')
#
#
# main()


# Эта программа имитирует 10-разовое подбрасывание монеты

import random

# Инициализируем КОНСТАНТЫ:
HEADS = 1       # Орел
TAILS = 2       # Решка
TOSSES = 10     # Количество бросков

# Пишем функцию:
def main():
    for toss in range(TOSSES):
        # Имитируем бросание монеты
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')

main()