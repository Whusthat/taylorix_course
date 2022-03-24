from tkinter import *
from random import shuffle


class PuzzlePiece(Button):
    position = 0
    value = int

    def click_event(self):
        top = None if self.position < puzzle.size else self.position - puzzle.size
        bottom = None if self.position >= (puzzle.size * (puzzle.size - 1)) else self.position + puzzle.size
        left = None if self.position % puzzle.size == 0 else self.position - 1
        right = None if (self.position + 1) % puzzle.size == 0 else self.position + 1
        # search if the stone is able to move and switch positions through turn method
        for piece in puzzle.btn_obj_list:
            if piece.position == top and piece.cget('text') == '':
                puzzle.turn(self, piece)
            elif piece.position == bottom and piece.cget('text') == '':
                puzzle.turn(self, piece)
            elif piece.position == left and piece.cget('text') == '':
                puzzle.turn(self, piece)
            elif piece.position == right and piece.cget('text') == '':
                puzzle.turn(self, piece)

    # representation for PuzzlePiece Object for debugging purposes
    def __repr__(self):
        return f"(pos:{self.position} | val:{self.value} )"


class Puzzle:

    def __init__(self, size):
        self.size = size
        self.grid = size ** 2
        self.btn_obj_list = []
        self.turn_count = 0
        self.root = Tk()
        self.root.title('Shuffle Puzzle')
        self.turn_counter = Label(self.root, text=f'Turns : {self.turn_count}', height=5)
        self.turn_counter.grid(row=(self.size * self.size + 1) // self.size, column=0)

    def turn(self, obj1, obj2):
        # increase counter each turn and print him in label
        self.turn_count += 1
        self.turn_counter.configure(text=f"Turns : {self.turn_count}")

        # calc new grid positions
        self_row = obj1.position // puzzle.size
        self_column = obj1.position % puzzle.size
        blank_row = obj2.position // puzzle.size
        blank_column = obj2.position % puzzle.size
        # assign new calculated positions
        position_holder = obj1.position
        obj1.position = obj2.position
        obj2.position = position_holder
        # remove buttons from grid
        obj1.grid_forget()
        obj2.grid_forget()
        # add them again with new positions
        obj1.grid(row=blank_row, column=blank_column)
        obj2.grid(row=self_row, column=self_column)
        # after every turn check if the win-condition is for-filled
        self.win_condition()

    def win_condition(self):
        sort_board = sorted(self.btn_obj_list, key=lambda obj: obj.position)
        # create a list with the order to win the puzzle
        win_order = [0 if x == self.grid else x for x in range(1, self.size * self.size+1)]
        print(win_order)
        # make the list to tuple for better comparing
        win_order = tuple(win_order)
        # generate a tuple of the current board state
        board_state = []
        for piece in sort_board:
            board_state.append(piece.value)
        board_state = tuple(board_state)

        if board_state == win_order:
            print('WIN')

    def count_inversion(self, liste):
        num_inversions = 0
        n = len(liste)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if liste[i] > liste[j] != 0:
                    num_inversions += 1
        return num_inversions

    def solve_order(self, liste):
        pos_sorted = sorted(liste, key=lambda o: o.position)
        if pos_sorted[0].value != 0 and pos_sorted[1].value != 0:
            temp = pos_sorted[0].position
            pos_sorted[0].position = pos_sorted[1].position
            pos_sorted[1].position = temp
        else:
            temp = pos_sorted[-1].position
            pos_sorted[-1].position = pos_sorted[-2].position
            pos_sorted[-2].position = temp

        return pos_sorted

    def shuffle_board(self, liste):
        # loop over object list and store position in list
        rnd_values = sorted(liste, key=lambda obj: obj.position)
        value_order = [x.value for x in rnd_values]
        print(value_order)
        empty_piece_row = str

        empty_piece = liste[-1]
        # check if the row containing empty puzzle piece is "odd" or "even"
        empty_piece_row = empty_piece.position // self.size
        empty_piece_row = 'odd' if empty_piece_row % 2 != 0 else 'even'

        inversion_count = self.count_inversion(value_order)

        if self.size % 2 == 0:
            # if odd we need to make sure that the amount of inversion is even
            if empty_piece_row == 'odd':
                if inversion_count % 2 == 0:
                    return liste
                else:
                    return self.solve_order(liste)
            # else we need to make sure that the amount inversion is odd
            else:
                if inversion_count % 2 != 0:
                    return liste
                else:
                    return self.solve_order(liste)
        else:
            if inversion_count % 2 == 0:
                return liste
            else:
                return self.solve_order(liste)

    def build_board(self):
        # create a list of integers each representing a position of a puzzle piece
        rnd_index_list = [int(x) for x in range(self.grid)]
        shuffle(rnd_index_list)
        # create randomized board
        # loop over every position on the board = size * size and give each button a position
        for i in range(1, self.grid + 1):
            # text equals the number on the puzzle piece
            # for position 0 we disable border and set background to white (#fff)
            if i == self.grid:
                button = PuzzlePiece(self.root, text='', width=10, height=5, bg='white', border=0)
            else:
                button = PuzzlePiece(self.root, text=i, width=10, height=5)
            position = rnd_index_list[0]
            value = button.cget('text') if button.cget('text') != '' else 0
            button.configure(command=lambda b=button: b.click_event())
            rnd_index_list.pop(0)
            button.position = position
            button.value = value
            self.btn_obj_list.append(button)
        print(self.btn_obj_list)
        self.shuffle_board(self.btn_obj_list)

        # assign the buttons to the gird
        for btn in self.btn_obj_list:
            # calc row and column position in grid
            row = btn.position // self.size
            column = btn.position % self.size
            btn.grid(row=row, column=column)

        self.root.mainloop()


def main():
    global puzzle
    puzzle = Puzzle(3)
    puzzle.build_board()


if __name__ == '__main__':
    main()