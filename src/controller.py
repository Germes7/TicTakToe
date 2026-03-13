from __future__ import annotations
from model.entities import Field
from model.constants import *

class Referee:

    __field: Field
    def __init__(self, field: Field):

        self.__field = field

    def check_win(self, marker) -> bool:  # Проверяет на победу
        pass

    def check_draw(self) -> bool:  # Проверяет на ничью
        pass

    def __check_win_by_row(self) -> bool:  # Проверка по строкам
        pass

    def __chck_win_by_column(self) -> bool:  # Проверка по столбцам
        pass

    def __check_win_by_diagonal(self) -> bool:  # Проверка по диагоналям
        pass


class Game:

    def __init__(self):

        self.__current_player = MARKER_EMPTY  # Игра знает о текущем игроке, кто сейчас ходит (по умолчанию Пустой маркер)

        self.__field = Field(3, 3)  # Игра создала поле
        self.referee = Referee(self.__field)  # Игра передала Судье знание о поле

    def set_up(self) -> None:  # Включиться (поле создайся)
        pass

    def make_move(self, x, y,) -> None:  # Попытка сделать ход
        pass

    def finish(self) -> None:  # Конец игре
        pass

