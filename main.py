from tkinter import *

#====================================================================
#               GUI CLASS FOR TIC TAC TOE BOARD
#====================================================================
class TicTacToe():
    # Initialize function
    def __init__(self):
        self.window = Tk()
        self.window.title('Project_03')
        self.canvas = Canvas(self.window, width=700, height=700)
        self.canvas.pack()

        # Game board needs to be initialized
        self.build_board()

    # Mainloop function
    def mainloop(self):
        self.window.mainloop()

    # Build board function
    def build_board(self):
        """Both for loops will create lines in the tkinter window
        to separate game spaces when playing against the AI"""
        # Creates two vertical lines
        for index in range(2):
            self.canvas.create_line((index + 1) * 700 / 3, 0, (index + 1) * 700 / 3, 700)
        # Creates two horizontal lines
        for index in range(2):
            self.canvas.create_line(0, (index + 1) * 700 / 3, 700, (index + 1) * 700 / 3)


if __name__ == '__main__':
    board = TicTacToe()
    board.mainloop()