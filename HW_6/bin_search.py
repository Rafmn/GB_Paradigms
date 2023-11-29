'''Бинарный поиск'''
from random import randint


def bin_search(sort_list: list, num: int) -> int:
    '''Бинарный поиск числа в списке. Если найден, возвращает его индекс.
    Иначе возвращает -1'''
    t_index = 0
    while len(sort_list) > 1:
        sort_list, start_index = check_num(sort_list, num, t_index)
        t_index += start_index  # Складываем индексы
        if isinstance(sort_list, int):
            return t_index
    if sort_list[0] == num:
        return t_index
    else:
        return -1


def check_num(a_list, num, start_index: int = 0):
    '''Принимает лист, число для поиска и начальный индекс.
    Возвращает в функцию bin_search() половину листа, в котором может 
    находиться искомое число и индекс для отсчета'''
    index_middl_list = len(a_list) // 2
    if a_list[index_middl_list] == num:
        return num, index_middl_list
    elif num < a_list[index_middl_list]:
        half_list = a_list[:index_middl_list]
        start_index = 0
    elif num > a_list[index_middl_list]:
        half_list = a_list[index_middl_list:]
        start_index = index_middl_list
    return half_list, start_index


if __name__ == ('__main__'):
    sorted_list = sorted([randint(1, 100)
                         for _ in range(50)])  # Генерация случайного списка
    num_search = randint(1, 100)  # Генерация случайного числа
    # print(sorted_list, num_search, sep='\n')
    print(bin_search(sorted_list, num_search))
