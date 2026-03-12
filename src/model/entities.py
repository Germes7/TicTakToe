from constants import *


class Cell:  # Клас Клетка

    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__marker = MARKER_EMPTY  # По умолчанию пустой маркер

    def get_x(self):  # Запрос координаты Х
        return self.__x

    def get_y(self):  # Запрос координаты Y
        return self.__y

    def is_empty(self) -> bool:  # Проверка пустая ли клетка?
        return self.__marker == MARKER_EMPTY

    def set_marker(self, marker: int) -> None:  # Установить маркер (x, 0)
        if marker != MARKER_ZERO and marker != MARKER_CROSS:
            raise ValueError(f"Не найден такой маркер {marker}")

        self.__marker = marker

    def reset(self) -> None:  # Сбросить клетку
        self.__marker = MARKER_EMPTY

