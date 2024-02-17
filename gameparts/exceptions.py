class FieldIndexError(IndexError):

    def __str__(self):
        return "Ввеедно значение за границами игрового поля"


class CellOccupiedError(Exception):

    def __str__(self):
        return "Попытка изменить занятую ячейку"
