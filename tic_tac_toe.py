import random
class game:
    def __init__(self):
        self.board = []
        for i in range(3):
            rows = []
            for j in range(3):
                rows.append("--")
            self.board.append(rows)
        print(self.board)
    
    
    def startGame(self):
        return random.randint(0, 1)

game = game()
game.startGame()