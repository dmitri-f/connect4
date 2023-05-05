def draw_board(board: list[list[str]]):
    print("Current board:")
    for row in board:
        print(" ".join(row))


def check_win(board: list[list[str]], rows, cols, win_num: int, curr_user: str) -> bool:
    # check horizontally
    for r in range(rows):
        for c in range(cols - win_num + 1):
            if all(board[r][c + i] == curr_user for i in range(win_num)):
                return True

    # check vertically
    for r in range(rows - win_num + 1):
        for c in range(cols):
            if all(board[r + i][c] == curr_user for i in range(win_num)):
                return True

    # check diagonally win (to right)
    for r in range(rows - win_num + 1):
        for c in range(cols - win_num + 1):
            if all(board[r + i][c + i] == curr_user for i in range(win_num)):
                return True

    # check diagonally win (to left)
    for r in range(rows - win_num + 1):
        for c in range(win_num - 1, cols):
            if all(board[r + i][c - i] == curr_user for i in range(win_num)):
                return True

    return False


def main():
    empty_sym = "_"
    rows, cols, win_num = 6, 7, 4
    board = [[empty_sym] * cols for _ in range(rows)]
    users = ["X", "O"]  # X - Red, O - Green
    curr_user = users[0]

    while True:
        draw_board(board)

        # read user input
        col = None
        while col is None:
            user_input = input(f"User \"{curr_user}\" move (choose column number: 1 to {cols}): ")
            try:
                user_input_int = int(user_input)
            except ValueError:
                print("Invalid input")
                continue

            if not (0 < user_input_int <= cols):
                print("Invalid column number")
                continue

            if board[0][user_input_int - 1] != empty_sym:
                print("This column is full, choose another one")
                continue

            col = user_input_int

        # make the move
        for r in range(rows - 1, -1, -1):
            if board[r][col - 1] == empty_sym:
                board[r][col - 1] = curr_user
                break

        # check for a win
        if check_win(board, rows, cols, win_num, curr_user):
            draw_board(board)
            print(f"User \"{curr_user}\" won!")
            break

        # check for a draw
        if all(board[0][c] != empty_sym for c in range(cols)):
            draw_board(board)
            print("Draw!")
            break

        # change current user
        curr_user_index = users.index(curr_user)
        curr_user = users[(curr_user_index + 1) % len(users)]


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
