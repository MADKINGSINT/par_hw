# Создаем доску
board = [' ' for _ in range(9)]

# Функция для отображения доски
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Функция для проверки выигрышной позиции
def check_win(player):
    win_combinations = [
        [0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8],  # Горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
        [0, 4, 8], [2, 4, 6]              # Диагонали
    ]
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Функция для осуществления хода игрока
def make_move(player):
    while True:
        position = input("Выберите позицию для хода (от 1 до 9): ")
        if not position.isdigit() or not (1 <= int(position) <= 9):
            print("Некорректный ввод!")
            continue
        index = int(position) - 1
        if board[index] != ' ':
            print("Эта позиция уже занята!")
            continue
        board[index] = player
        break

# Основной игровой цикл
def play_game():
    player = 'X'
    while True:
        display_board()
        make_move(player)
        if check_win(player):
            display_board()
            print("Игрок", player, "победил!")
            break
        if ' ' not in board:
            display_board()
            print("Ничья!")
            break
        player = 'O' if player == 'X' else 'X'

# Запуск игры
play_game()
