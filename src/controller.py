from __future__ import annotations
from model.entities import Field

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