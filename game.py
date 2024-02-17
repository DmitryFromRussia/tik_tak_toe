from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')  


def main():
    # Создаем игровое поле объектом нашего класса:
    game = Board()
    current_player = "X"
    running = True
    # Отрисовываем поле в терминале.
    game.display()

    while running:

        print(f"Ход делаает {current_player}")

        while True:
            try:
                row = int(input("Введите номаер строки: "))
                if row < 0 or row >= game.field_size:
                    # "выбрасывание" исключения FieldExceptionError
                    raise FieldIndexError
                column = int(input("Введите номер столбца: "))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    "Значение должно быть неотрицательным и меньше "
                    f"{game.field_size}."
                )
                print("Пожалуйста, введите значения для строки и столбца заново!")
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
            except ValueError:
                print("Буквы вводить нельзя, только числа!")
                print("Пожалуйста, введите значение для строки и столбца.")
            except Exception as ex:
                print(f"Возникла непредвиденная ошибка: {ex}")
            else:
                break
        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            result = f'Победили {current_player}!'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья'
            print(result)
            save_result(result)
            running = False
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = "O" if current_player == "X" else "X"
    # Разместим на поле символ по указанным кооридинатам: мы сделали ход!


if __name__ == "__main__":
    main()
