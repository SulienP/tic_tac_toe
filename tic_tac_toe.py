import random
import connect 
class game:
    def __init__(self):
        self.board = []
        for i in range(3):
            rows = []
            for j in range(3):
                if j == 2:
                    rows.append("-")
                else:
                    rows.append("-|")
            self.board.append(rows)

    
    def endGame(array):
        # check diago
        if array[0][0] == array[1][1] == array[2][2] or array[0][2] == array[1][1] == array[2][0]:
            if array[1][1] == "X":
                return "X"
            elif array[1][1] == "O":
                return "O"
        # check rows
        for i in range(3):
            if array[i][0] == array[i][1] == array[i][2]:
                if array[i][0] == "X":
                    return "X"
                else :
                    return "0"
        #check columns
        for v in range(3):
            if array[0][v] == array[1][v] == array[2][v]:
                if array[0][v] == "X":
                    return "X"
                elif array[0][v] == "O":
                    return "O"
        
                 
    def isWin(array):
        value = endGame(array)
        if value =="x":
            return True
        else: 
            return False
        
    def updateTicTacToe(array, value):
        for i in range(value[1] - 1):
            for j in range(value[0] -1):
                array[i][j] = value[0][1]
                return array
game = game()
game.startGame()