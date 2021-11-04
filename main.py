import tkinter
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
        # Player will alternate between X and O
        self.player = 'X'
        # Game board needs to be initialized
        self.build_board()
        # Will need a list to know the current layout of the board to verify a winner
        self.board_layout = [['','',''],['','',''],['','','']]

    # Mainloop function
    def mainloop(self):
        self.window.mainloop()

    # Function applies Xs and Os when button pressed
    def select_tile(self, button, row, col):
        # This is to handle if the current player is
        # the computer
        if self.player == 'X':
            # Run a check to see if the button is available
            if button["text"] == "":
                button["text"] = "X"
                # Update the board list
                self.board_layout[row][col] = 'X'
            # converts to O
            self.player = 'O'
        # Here, if the player is human, after click convert to X
        # so that the computer can make a move
        elif self.player == 'O':
            # Run a check to see if the button is available
            if button["text"]== "":
                button["text"]="O"
                # Update the board list
                self.board_layout[row][col] = 'O'
            # converts to X
            self.player = 'X'

        # Increase count by 1
        self.count += 1
        # If count greater than 5, a winner may exist
        if self.count >= 5:
            # check for winning line
            self.checkForWinner()

    # Function will run through all scenarios of winning to determine if there is yet a winner
    # or if it ends in a tie!
    def checkForWinner(self):
        # This checks if X's win
        if (self.board_layout[0][0]==self.board_layout[0][1]==self.board_layout[0][2]=='X' or
            self.board_layout[1][0]==self.board_layout[1][1]==self.board_layout[1][2]=='X' or
            self.board_layout[2][0]==self.board_layout[2][1]==self.board_layout[2][2]=='X' or
            self.board_layout[0][0]==self.board_layout[1][0]==self.board_layout[2][0]=='X' or
            self.board_layout[0][1]==self.board_layout[1][1]==self.board_layout[2][1]=='X' or
            self.board_layout[0][2]==self.board_layout[1][2]==self.board_layout[2][2]=='X' or
            self.board_layout[0][0]==self.board_layout[1][1]==self.board_layout[2][2]=='X' or
            self.board_layout[0][2]==self.board_layout[1][1]==self.board_layout[2][0]=='X'):
            # Print Winner
            self.show_winner("Player X")
            return True

        # This checks if the O's win
        elif(self.board_layout[0][0]==self.board_layout[0][1]==self.board_layout[0][2]=='O' or
            self.board_layout[1][0]==self.board_layout[1][1]==self.board_layout[1][2]=='O' or
            self.board_layout[2][0]==self.board_layout[2][1]==self.board_layout[2][2]=='O' or
            self.board_layout[0][0]==self.board_layout[1][0]==self.board_layout[2][0]=='O' or
            self.board_layout[0][1]==self.board_layout[1][1]==self.board_layout[2][1]=='O' or
            self.board_layout[0][2]==self.board_layout[1][2]==self.board_layout[2][2]=='O' or
            self.board_layout[0][0]==self.board_layout[1][1]==self.board_layout[2][2]=='O' or
            self.board_layout[0][2]==self.board_layout[1][1]==self.board_layout[2][0]=='O'):
            # Print the winner
            self.show_winner("Player O")
            return True

        # This will run if all tiles are selected and there is no winner
        elif(self.count == 9):
            self.show_winner("It's a Tie!!")
            return True

        return False

    # Display who the winner is
    def show_winner(self, winner):
        self.win = Tk()
        self.win.title("You Won!!!")
        self.win.configure(bg="Black")
        self.win.geometry("300x300")

        # Make the pop up the focus and disable the board
        self.win.focus_set()
        self.window.attributes('-disabled', True)

        # Print the result to the new window
        if winner == "It's a Tie!!":
            # Build the label
            label_01 = Label(self.win, text=winner, font="Helvetica 16 bold", bg="Black", fg="White")
            # Pack the label
            label_01.pack(side=tkinter.TOP, pady=50)
        else:
            # Build the label
            label_01 = Label(self.win, text=winner, font="Helvetica 16 bold", bg="Black", fg="White")
            # Pack the label
            label_01.pack(pady=25)
            label_02 = Label(self.win, text="Has Won!!", font="Helvetica 16 bold", bg="Black", fg="White")
            label_02.pack(pady=25)

        # Button causes all open windows to be destroyed
        end_button = Button(self.win, text="End", font="Helvetica 12 bold", command=self.destroyWindow)
        end_button.pack(side=tkinter.BOTTOM, pady=50)

    # Window destroy function
    def destroyWindow(self):
        # Destroy the board
        self.window.destroy()
        # Destroy the message box
        self.win.destroy()

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

    # Create the minimax algorithm for alpha-beta prunning
    def minimax(self):
        pass

#====================================================================
#                          Main Program
#====================================================================
if __name__ == '__main__':
    board = TicTacToe()
    board.mainloop()