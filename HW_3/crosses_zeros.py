'''Консольная игра в крестики-нолики'''
from random import randint


class SomeList:
    """Листок с крестиками-ноликами"""

    def __init__(self):
        self.empty_list = []

    def generate_empty_list(self):
        """Генерация и вывод пустого листа"""
        num = 1
        while num <= 9:
            for _ in range(3):
                list_i = []
                for _ in range(3):
                    list_i.append(num)
                    num += 1
                self.empty_list.append(list_i)

    def show_list(self):
        """Вывод листа"""
        for i in self.empty_list:
            print(*i)

    def move(self, move):
        """Ход игрока"""
        move = self.check_move(move)
        i = move // 3
        if move % 3 == 0:
            i -= 1
        j = move % 3 - 1
        self.empty_list[i][j] = 'X'

    def check_move(self, move):
        '''Проверка корректности ввода'''
        i = move // 3
        if move % 3 == 0:
            i -= 1
        j = move % 3 - 1
        while not isinstance(self.empty_list[i][j], int):
            try:
                move = int(
                    input('Эта клетка занята, выберите другую клетку: '))
                i = move // 3
                if move % 3 == 0:
                    i -= 1
                j = move % 3 - 1
            except ValueError:
                print('Вы ввели не число')
        return move

    def bot_move(self):
        '''Ход бота'''
        move = randint(1, 9)
        i = move // 3
        if move % 3 == 0:
            i -= 1
        j = move % 3 - 1
        while not isinstance(self.empty_list[i][j], int):
            move = randint(1, 9)
            i = move // 3
            if move % 3 == 0:
                i -= 1
            j = move % 3 - 1
        self.empty_list[i][j] = 'O'

    def check_list(self):
        '''Проверка выигрышной позиции'''
        for i in range(3):
            for j in range(3):
                if self.empty_list[0][j] == self.empty_list[1][j] == self.empty_list[2][j]:
                    return True
                elif self.empty_list[i][0] == self.empty_list[i][1] == self.empty_list[i][2]:
                    return True
                elif self.empty_list[0][0] == self.empty_list[1][1] == self.empty_list[2][2]:
                    return True
                elif self.empty_list[0][2] == self.empty_list[1][1] == self.empty_list[2][0]:
                    return True


if __name__ == ('__main__'):
    a_list = SomeList()
    a_list.generate_empty_list()
    a_list.show_list()
    my_move = None
    count_move = 0
    while my_move != 'stop' and count_move < 9:
        my_move = input('Введите номер нужной клетки для хода или stop: ')
        if my_move == 'stop':
            break
        a_list.move(int(my_move))
        a_list.show_list()
        if a_list.check_list():
            print('You won')
            break
        count_move += 1
        if count_move == 9:
            break
        print('Ход бота:')
        a_list.bot_move()
        a_list.show_list()
        if a_list.check_list():
            print('Bot won')
            break
        count_move += 1

    print('Over game')
