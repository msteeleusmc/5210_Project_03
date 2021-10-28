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


    # Mainloop function
    def mainloop(self):
        self.window.mainloop()

if __name__ == '__main__':
    board = TicTacToe()
    board.mainloop()