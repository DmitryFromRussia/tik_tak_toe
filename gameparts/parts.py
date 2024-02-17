# Создаем игру кретики - нолики.
# Объявляем класс:
class Board:
    """Класс, описывающий игровое поле."""

    field_size = 3

    # Иициализиурем игровое поле - списиок списков с пробелами.
    # Пробелы - пустые клетки.
    def __init__(self):
        self.board = [[" " for i in range(3)] for i in range(3)]
        """Раскладываем эту строчку для понимания:
        self.board = []
        for i in range(3):
            board = []
            for i in range(3):
                board.append(' ')
            self.board.append(board)"""

    # Метод, обрабатывающий ходы игроков:
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, отрисовывающий игровое поле:
    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
            
    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True
    
    def check_win(self, player):
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                all([self.board[j][i] == player for j in range(3)])):
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False

    def __str__(self):
        return "Объект игровокого поля размером" f"{self.field_size}x{self.field_size}"
