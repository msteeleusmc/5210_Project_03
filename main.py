import tkinter as tk
import random
from tkinter import messagebox
import math
from tkinter import *


#====================================================================
#                           Global Functions
#====================================================================
alphaValue = -math.inf
betaValue = math.inf

# Function starts the program
def startProgram():
    # Assign the root
    root = tk.Tk()
    # Pack the board
    TicTacToe(root).pack(fill="both", side="top", expand=True)
    # Start the loop
    root.mainloop()

# Assigns either an X or an O to the location based on whose turn it is
def assignSymbol(turn_order):
    # If the ai is the current player
    if(turn_order): return 'X'
    # If the humna is the current player
    return 'O'

# Function will update the board
def updateBoard(current, row, col, value):
    # Calls assignSymbol function to assign either X or O based on who the current player is
    current[row * 3 + col] = assignSymbol(value)
    # value is passed as a boolean so if True then return False
    return not value

# Checks for if there is a Tie
def gameDraw(current: list):
    # If no winner was declared and -1 is not in the list
    return -1 not in current

# minimax algorithm to find best AI move
def minimaxAlgorithm(curr, is_ai, value):
    global alphaValue
    global betaValue
    # Returns score
    if isWon(curr): return curr, 1 + finalScore(curr) if not is_ai else -finalScore(curr) - 1
    # Returns a score of 0
    if gameDraw(curr): return curr, 0
    # Function generates possible moves
    poss_moves = generatePossibleMoves(curr, value)
    miniMaxScore = -1000 if is_ai else 1000
    next_move = None
    for move in poss_moves:
        temp_next_move, score = minimaxAlgorithm(move, not is_ai, not value)
        if (score > miniMaxScore and is_ai) or (score < miniMaxScore and not is_ai):
            next_move, miniMaxScore = move, score

    if(is_ai): alphaValue = miniMaxScore
    else: betaValue = miniMaxScore

    return next_move, miniMaxScore

# Checks if algo is winner then returns to miniMax
def isWon(curr: list):
    for i in range(3):
        if curr[3 * i + 0] == curr[3 * i + 1] == curr[3 * i + 2] != -1: return True
        if curr[0 + i] == curr[3 + i] == curr[6 + i] != -1: return True
    return curr[0] == curr[4] == curr[8] != -1 or curr[2] == curr[4] == curr[6] != -1

def finalScore(curr):
    res = 0
    for x in curr:
        if x == -1: res += 1
    return res

# Possible move generator
def generatePossibleMoves(curr, value):
    temp_symbol = assignSymbol(value)
    possible_moves = []
    for i, x in enumerate(curr):
        if x == -1:
            possible_moves.append(curr[:])
            possible_moves[-1][i] = temp_symbol
    random.shuffle(possible_moves)
    return possible_moves

#====================================================================
#                           Main GUI Class
#====================================================================
class TicTacToe(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Establish parent variables
        parent.minsize(700, 700)
        parent.title("Project 03")

        self.new_game = tk.Button(self, width=10, height=3, text="New Game", bg="gray", fg="black", command=self.clearBoard)
        self.new_game.pack(side=tk.BOTTOM, anchor=tk.CENTER, pady=60)
        # Call child class to build game board
        self.board_layout = BuildBoard(self)

    # Function called when New Game button is clicked.
    def clearBoard(self):
        # resetBoard function is then called to clear the board and start an new game
        self.board_layout.resetBoard(disable=False)

#====================================================================
#                           Game Board GUI Class
#====================================================================
class BuildBoard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        global alphaValue
        global betaValue

        # Will need a list to know the current layout of the board to verify a winner
        self.board_layout = [[], [], []]
        # Function called to build the board
        self.buildBoard(3)
        tk.Label(parent).pack()
        # Score tracker at the top of the window
        self.score = tk.Label(parent, text="")
        self.score.pack()
        self.betaScore = tk.Label(parent, text="")
        self.betaScore.pack(side=tk.BOTTOM, anchor=tk.NW, pady=15, padx=45)
        self.pack(pady=15)
        self.alphaScore = tk.Label(parent, text="")
        self.alphaScore.pack(side=tk.BOTTOM, anchor=tk.NW, padx=45)

        # Establishes AI's first move
        self.setAiPosition()

    def buildBoard(self, length):
        # Place buttons as grid squares
        for i in range(length):
            for j in range(length):
                self.board_layout[i].append(self.addButton())
                # Lambda function then calls the fillBoard() function
                self.board_layout[i][j].config(command=lambda row=i, col=j: self.fillBoard(row, col))
                self.board_layout[i][j].grid(row=i, column=j)

    # Fill board function
    def fillBoard(self, row, col):
        self.board_layout[row][col].config(text=assignSymbol(self.turn), state=tk.DISABLED, bg="black", fg="white")
        self.ai_value[row * 3 + col] = assignSymbol(self.turn)
        # Check if end of game with the human player
        check_status = self.checkIfGameHasEnded("Player")
        # If check_status is True because there is a winner/tie then this function
        # will return breaking the game loop
        if check_status: return
        # Otherwise fillBoard function continues here
        self.turn = updateBoard(self.ai_value, row, col, self.turn)
        self.aiPlayerTurn()

    # Function adds a button to tile space
    def addButton(self):
        newButton = tk.Button(self, width=11, height=4, bg="gray", font=('Helvetica', 24, 'bold'))
        return newButton

    # Called to set up the AI's first move choice randomly
    def setAiPosition(self):
        # Sets a list to all -1
        self.ai_value = [-1] * 9
        # AI turn is True
        self.turn = True
        # AI Player given random first move
        aiPlayerTurn = random.choice([0,1,2,3,4,5,6,7,8])
        # move is a list of all -1
        move = self.ai_value[:]
        # move choice is assigned with an X
        move[aiPlayerTurn] = 'X'
        # List move is then sent to aiPlayerTurn
        self.aiPlayerTurn(move)

    # Player and Computer are passed to this function as strings
    def checkIfGameHasEnded(self, player):
        winner = self.checkForWinner()
        if winner:
            # If winner is True, then message box prints result
            messagebox.showinfo("", "{} has won".format(player))
            return True
        # gameDraw() function checks for a tie between human and AI
        if gameDraw(self.ai_value):
            # Message box will print result
            messagebox.showinfo("", "It's a Draw")
            return True
        # Return False if there is no winner or tie
        return False

    # Function is called when it is the computers turn
    def aiPlayerTurn(self, start=None):
        # Initially, start is assigned the list from first AI move
        if start:
            # Ai first move is equal to start
            player_move = start
            # Initial score is 0
            score = 0
        # After first move, start == None
        else:
            # Function returns
            player_move, score= minimaxAlgorithm(self.ai_value, True, self.turn)
        self.score.config(text="minimax score {}".format(score))
        self.alphaScore.config(text="Alpha Score {}".format(alphaValue))
        self.betaScore.config(text="Beta Score {}".format(betaValue))
        index = 0
        for i in range(9):
            if self.ai_value[i] != player_move[i]:
                index = i
                break
        self.ai_value = player_move
        self.board_layout[index // 3][index % 3].config(text=assignSymbol(self.turn), state=tk.DISABLED, fg="white", bg="red")
        self.turn = not self.turn
        self.checkIfGameHasEnded("Computer")

    # This is the actual function to check for a winner between computer and human
    def checkForWinner(self):
        curr = self.ai_value
        if(curr[0] == curr[1] == curr[2] != -1): return True
        if(curr[3] == curr[4] == curr[5] != -1): return True
        if(curr[6] == curr[7] == curr[8] != -1): return True
        if(curr[0] == curr[3] == curr[6] != -1): return True
        if(curr[1] == curr[4] == curr[7] != -1): return True
        if(curr[2] == curr[5] == curr[8] != -1): return True
        if(curr[0] == curr[4] == curr[8] != -1): return True
        if(curr[6] == curr[4] == curr[2] != -1): return True
        # Return False if none of the above are True
        return False

    # Called from the TicTacToe class if New Game button is clicked to reset the board
    def resetBoard(self, disable=True):
        for i in range(3):
            for j in range(3):
                if disable:
                    self.board_layout[i][j].config(state=tk.DISABLED, bg="gray", fg="black")
                else:
                    self.board_layout[i][j].config(text="", bg="gray", fg="black", state=tk.NORMAL)
        if not disable: self.setAiPosition()

        self.alphaScore.config(text="Alpha Score {}".format(-math.inf))
        self.betaScore.config(text="Beta Score {}".format(math.inf))

#====================================================================
#                           Main Program
#====================================================================
if __name__ == '__main__':
    startProgram()
