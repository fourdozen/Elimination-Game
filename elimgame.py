
class Critter:
    def __init__(self, cell_number, is_up):
        self.cell_number = cell_number
        self.is_up = is_up
        self.x_pos = cell_number % N
        self.y_pos = cell_number // N

    def flip_state(self):
        # flips/switches state
        self.is_up = not self.is_up

    def get_adjacent(self):
        # outputs cell numbers of adjacent cells
        out = []
        if self.x_pos >= 1:
            out.append(get_cell_num(self.x_pos - 1, self.y_pos, N))
        if self.x_pos + 1 <= (N - 1):
            out.append(get_cell_num(self.x_pos + 1, self.y_pos, N))

        if self.y_pos >= 1:
            out.append(get_cell_num(self.x_pos, self.y_pos - 1, N))
        if self.y_pos + 1 <= (N - 1):
            out.append(get_cell_num(self.x_pos, self.y_pos + 1, N))

        return tuple(out)


def create_board(n, critter_pos_list):
    board = []

    for i in range(n ** 2):
        x = i in critter_pos_list
        board.append(Critter(i, x))

    return board


def print_board(board, n):
    c_state_dict = {True: "up",
                    False: "down"}

    for i in range(n ** 2):
        print(f"{c_state_dict[board[i].is_up]:7}", end=" ")
        if i % n == (n - 1):
            print(" ")
    print(" ")


def get_cell_num(x, y, n):
    return y * n + x


def is_solved(board):
    for i in board:
        if i.is_up:
            return False
    return True


def critter_is_hit(board, cell_to_flip):
    board[cell_to_flip].flip_state()
    for c in board:
        if c.cell_number in board[cell_to_flip].get_adjacent():
            c.flip_state()

    return board


def print_empty_board(n):
    # print("Positions on the board")
    for i in range(n ** 2):
        print(f"{i:4d}", end=" ")
        if i % n == (n - 1):
            print(" ")
