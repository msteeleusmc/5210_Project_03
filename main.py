from tkinter import *

#====================================================================
#               GUI CLASS FOR TIC TAC TOE BOARD
#====================================================================
class TicTacToe():
    # Initialize function
    def __init__(self):
        # Build the window for the game
        self.window = Tk()
        self.window.title('Project_03')
        self.canvas = Canvas(self.window, width=700, height=700)
        # Requires a global count of spaces
        self.count = 0
        # Game board needs to be initialized
        self.build_board()
        # Will need a list to know the current layout of the board to verify a winner
        self.board_layout = [['','',''],['','',''],['','','']]

    # Mainloop function
    def mainloop(self):
        self.window.mainloop()

    # Function applies Xs and Os when button pressed
    def select_tile(self, button, row, col):
        # Run a check to see if the button is available
        if button["text"]== "":
            if self.count % 2 == 0:
                button["text"]="X"
                # Update the board list
                self.board_layout[row][col] = 'X'
            else:
                button["text"]="O"
                # Update the board list
                self.board_layout[row][col] = 'O'

            # Increase count by 1
            self.count += 1
            # If count greater than 5, a winner may exist
            if self.count >= 5:
                # check for winning line
                self.checkForWinner()

    def checkForWinner(self):
        pass


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

        # Grid buttons for the board
        b1 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b1, 0, 0))
        b2 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b2, 0, 1))
        b3 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b3, 0, 2))
        b4 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b4, 1, 0))
        b5 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b5, 1, 1))
        b6 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b6, 1, 2))
        b7 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b7, 2, 0))
        b8 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b8, 2, 1))
        b9 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Helvetica 16 bold", command=lambda: self.select_tile(b9, 2, 2))

        # Establish the actual buttons row and col locations
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)
        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=3, column=0)
        b8.grid(row=3, column=1)
        b9.grid(row=3, column=2)

#====================================================================
#                          Main Program
#====================================================================
if __name__ == '__main__':
    board = TicTacToe()
    board.mainloop()