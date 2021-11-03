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
        #self.canvas.pack()

        # Game board needs to be initialized
        self.build_board()


    # Mainloop function
    def mainloop(self):
        self.window.mainloop()


    def change_value(self,button,boardValRow,boardValCol):
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
                        font="Times 15 bold", command=lambda: self.change_value(b1, 0, 0))
        b2 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b2, 0, 1))
        b3 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b3, 0, 2))
        b4 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b4, 1, 0))
        b5 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b5, 1, 1))
        b6 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b6, 1, 2))
        b7 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b7, 2, 0))
        b8 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b8, 2, 1))
        b9 = Button(self.window, text="", height=8, width=16, bg="gray", activebackground="white", fg="white",
                        font="Times 15 bold", command=lambda: self.change_value(b9, 2, 2))

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



        """
        b2 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b2, 0, 1))
        b3 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b3, 0, 2))
        b4 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b4, 1, 0))
        b5 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b5, 1, 1))
        b6 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b6, 1, 2))
        b7 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b7, 2, 0))
        b8 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b8, 2, 1))
        b9 = Button(self.window(), text="", height=4, width=8, bg="black", activebackground="white", fg="white",
                    font="Times 15 bold", command=lambda: self.change_value(b9, 2, 2))
        """

if __name__ == '__main__':
    board = TicTacToe()
    board.mainloop()