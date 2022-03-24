from tkinter import *
from random import shuffle


class Game:

    def __init__(self):
        self.rounds = 0
        self.round = GameRound()
        start_frame.pack_forget()


class GameRound:

    def __init__(self):
        # init input frame
        self.input_frame = Frame(root, pady=10, padx=10)
        self.input_frame.pack(side=BOTTOM)
        self.user_input()

    def user_input(self):
        # declaring widgets
        grid_size_input = Label(self.input_frame, text='Please enter the size of the Puzzle', font=('Arial', 14))
        submit_btn = Button(self.input_frame, text='Continue', width=8, height=2, font=('Arial', 14),
                            command=lambda: self.validate_input(grid_size_input_wrapper.get(), message))
        grid_size_input_wrapper = Entry(self.input_frame, validate="all")
        message = Label(self.input_frame, text='', font=('Arial', 14))

        # arrange widgets
        grid_size_input.grid(row=0, column=1)
        grid_size_input_wrapper.grid(row=1, column=1)
        submit_btn.grid(row=3, column=1, pady=20)
        message.grid(row=2, column=1)

    def validate_input(self, user_input, label_obj):
        try:
            number = int(user_input)
            board = Board(number)
            self.input_frame.pack_forget()

        except ValueError:
            label_obj.configure(text='you monkey thats not a number')


class Board:

    def __init__(self, size):
        self.size = size
        self.grid_size = self.size ** 2
        self.tile_list = []
        self.board_window = Frame(root)
        self.build_tiles()
        self.shuffle_board(self.tile_list)

    def turn(self, obj1, obj2):

        # calc new grid positions
        self_row = obj1.position // self.size
        self_column = obj1.position % self.size
        blank_row = obj2.position // self.size
        blank_column = obj2.position % self.size

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
        'self.win_condition()'

    def build_tiles(self):
        random_index = [int(x) for x in range(self.grid_size)]
        shuffle(random_index)
        for i in range(1, self.grid_size + 1):
            tile = Tiles(self.board_window, text=i, width=10, height=5)
            tile.configure(command=lambda b=tile: b.click(self))
            tile.position = random_index[0]
            tile.value = i
            random_index.pop(0)
            self.tile_list.append(tile)

            # assign the buttons to the grid
            row = tile.position // self.size
            column = tile.position % self.size
            tile.grid(row=row, column=column)

        self.tile_list[-1].config(text='', bg='white', border=0)
        self.tile_list[-1].value = 0
        self.board_window.pack()

    def shuffle_board(self, list_of_obj):
        sorted_list = sorted(list_of_obj, key=lambda o: o.position)
        inversion_values = [x.value for x in sorted_list]

        empty_tile = None
        for obj in sorted_list:
            if obj.value == 0:
                empty_tile = obj
        empty_tile_row = empty_tile.position // self.size
        empty_tile_row_parity = 'odd' if empty_tile_row % 2 != 0 else 'even'

        inversion_count = self.count_inversion(inversion_values)

        if self.size % 2 == 0:
            # if odd we need to make sure that the amount of inversion is even
            if empty_tile_row_parity == 'odd':
                if inversion_count % 2 == 0:
                    return list_of_obj
                else:
                    return self.solve_order(list_of_obj)
            # else we need to make sure that the amount inversion is odd
            else:
                if inversion_count % 2 != 0:
                    return list_of_obj
                else:
                    return self.solve_order(list_of_obj)
        else:
            if inversion_count % 2 == 0:
                return list_of_obj
            else:
                return self.solve_order(list_of_obj)

    @staticmethod
    def count_inversion(liste):
        num_inversions = 0
        n = len(liste)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if liste[i] > liste[j] != 0:
                    num_inversions += 1
        return num_inversions

    @staticmethod
    def solve_order(liste):
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


class Tiles(Button):
    position = 0
    value = int

    def click(self, board_obj):
        top = None if self.position < board_obj.size else self.position - board_obj.size
        bottom = None if self.position >= (board_obj.size * board_obj.size - 1) else self.position + board_obj.size
        left = None if self.position % board_obj.size == 0 else self.position - 1
        right = None if (self.position + 1) % board_obj.size == 0 else self.position + 1
        # search if the stone is able to move and switch positions through turn method
        for piece in board_obj.tile_list:
            if piece.position == top and piece.cget('text') == '':
                board_obj.turn(self, piece)
            elif piece.position == bottom and piece.cget('text') == '':
                board_obj.turn(self, piece)
            elif piece.position == left and piece.cget('text') == '':
                board_obj.turn(self, piece)
            elif piece.position == right and piece.cget('text') == '':
                board_obj.turn(self, piece)

    # representation for PuzzlePiece Object for debugging purposes
    def __repr__(self):
        return f"(pos:{self.position} | val:{self.value} | cget: {self.cget('text')})"


if __name__ == '__main__':
    root = Tk()
    # init start frame
    start_frame = Frame(root, padx=10, pady=10)
    root.title('Shuffle Puzzle for degens only!')
    start_img = PhotoImage(file="assets/img.png")
    start_label = Label(start_frame, image=start_img)
    start_tile = Label(start_frame, text='The one and only Puzzle for degens', font=('Arial', 16), pady=20)
    start_btn = Button(start_frame, text='Start', width=8, height=3, font=('Arial', 14), command=lambda: Game())
    start_btn.pack(side=BOTTOM)
    start_tile.pack(side=TOP)
    start_label.pack(side=TOP)
    start_frame.pack()
    root.mainloop()
