'''Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами).'''

from random import randint
import numpy


def pearson_correlation(mass_x: list, mass_y: list) -> float:
    '''Функция вычисления коэффициента корреляции Пирсона'''
    # Вычисляем суммы массивов:
    sum_x = sum(mass_x)
    sum_y = sum(mass_y)

    # Среднеарифметическое:
    middle_x = sum_x / len(mass_x)
    middle_y = sum_y / len(mass_y)

    # Отклонения от среднеарифметического:
    # otkl_mass_x = [middle_x - i for i in mass_x]
    # otkl_mass_y = [middle_y - i for i in mass_y]
    otkl_mass_x = list(map(lambda x: middle_x - x, mass_x))
    otkl_mass_y = list(map(lambda y: middle_y - y, mass_y))

    # Возводим в квадрат каждое отклонение:
    # quart_x = [i ** 2 for i in otkl_mass_x]
    # quart_y = [i ** 2 for i in otkl_mass_y]
    quart_x = list(map(lambda x: x ** 2, otkl_mass_x))
    quart_y = list(map(lambda y: y ** 2, otkl_mass_y))

    # Сумма квадратов этих отклониний:
    sum_quart_x = sum(quart_x)
    sum_quart_y = sum(quart_y)

    # Произведение среднеарифметических значений массивов:
    multy_middle_xy = list(map(lambda x, y: x * y, otkl_mass_x, otkl_mass_y))

    # Сумма этих произведений:
    sum_mul_xy = sum(multy_middle_xy)

    # Подставляем найденые значения в формулу Пирса:
    r_xy = sum_mul_xy / ((sum_quart_x * sum_quart_y) ** 0.5)

    return r_xy


if __name__ == ("__main__"):
    # set_x = [randint(1, 100) for i in range(20)]
    # set_y = [randint(1, 100) for i in range(20)]
    list_x = list(map(lambda x: randint(1, 100), range(20)))
    list_y = list(map(lambda y: randint(1, 100), range(20)))

    print(list_x, list_y, sep='\n')  # Заданный массив
    print(pearson_correlation(list_x, list_y))  # Функциональное вычисление
    # Проверка результата через модуль библиотеки numpy
    print(numpy.corrcoef(list_x, list_y))
