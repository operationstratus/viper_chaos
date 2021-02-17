n = 5
# n x n

b = 10
# boats


HITS = 0

BOOMS = 0




class Tile:
    def __init__(self, boat=False):
        self.__boat = boat
        self.__character = " "
    
    def shoot(self):
        if self.__boat:
            self.__character = "x"
        return self.__boat # returns true if there indeed was a boat here, but false if there was none
    
    def get_character(self):
        return self.__character



def setup():
    BattleMap = [] # list with all the Tiles
    i = 0
    for w in range(n):
        for h in range(n):
            print(str(i))
            i += 1 # bara för att testa att for loopen funkar
            if corresponding tile in the text file has ha boat on this tile number:
                boat = True
            else:
                boat = False
            BattleMap.append(Tile(boat))
    return BattleMap

def update(BattleMap):
    i = 0
    for Tile in BattleMap:
        here print the right amount of "|" and "-" and " " in some clever way
        
        print(Tile.get_character())
       
        if i % 5 == 0: # if we have just made a sixth tile, we should begin next row
            print("\n") # begin a new row

def main():
    BattleMap = setup()
    while not wanting to quit:
        some if statements to navigate between options
        
        when you shoot:
        print("What coordinates do you want to shoot at?")
        x = input("x: ")
        y = input("y: ")
        tile_index = x + n*y
        
        if BattleMap[tile_index].shoot() == True:
            HITS += 1
        else:
            BOOMS += 0
            
    update(BattleMap)
        


        
            
            
