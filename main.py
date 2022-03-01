import os
import map


def ClearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

isPlaying = True

x_position = 5
y_position = 1

# Player class
class Player:
    def __init__(self):
        self.Input()

    def PlayerLoop(self):
        self.Input()

    def Input(self):
        print("Input")
        inputs = input()
        
        if inputs == "a" or inputs == "A":
            self.Position(x_position - 1, y_position)

        if inputs == "d" or inputs == "D":
            self.Position(x_position + 1, y_position)

        if inputs == "w" or inputs == "W":
            self.Position(x_position, y_position + 1)

        if inputs == "s" or inputs == "S":
            self.Position(x_position, y_position - 1)

        if inputs == "exit":
            isPlaying = False
            
    def Position(self, _x_position, _y_position):
        
        print(x_position)
        print(y_position)

class DrawMapClass:    
    def __init__(self):
        self.DrawMap(1)

    def MapLoop(self):
        self.DrawMap(1)

    def GetRow(self, area, row):
        getRow = map.GetGlobalVariable("list_" + str(area) + "_" + str(row))
        return getRow
    
    def DrawMap(self, area):
        mapHeight = map.mapHeight
        drawOrder = 1
        list = ""
    
        while mapHeight > 0:
            rowToDraw = self.GetRow(area, drawOrder)
            print(list.join(rowToDraw))
            mapHeight -= 1
            drawOrder += 1

player = Player()
map = DrawMapClass()

while isPlaying:
    player.PlayerLoop()
    map.__init__()