from src.dofus.direction import Direction

class MapHint:
    def __init__(self,pos):
        self.pos = pos
        self.right = None
        self.left = None
        self.down = None
        self.up = None
        self.hints = []
        
    def add_map_direction(self, direction, maphint):
        if (Direction(direction) == Direction.right):
            self.right = maphint
        elif (Direction(direction) == Direction.left):
            self.left = maphint
        elif (Direction(direction) == Direction.down):
            self.down = maphint
        elif(Direction(direction) == Direction.up):
            self.up = maphint
        
    def add_hint(self, hint):
        self.hints.append(hint)
        
    def get_directon(self,direction):
        if (Direction(direction) == Direction.right):
            return self.right
        elif (Direction(direction) == Direction.left):
            return self.left
        elif (Direction(direction) == Direction.down):
            return self.down
        elif(Direction(direction) == Direction.up):
            return self.up
        
    def get_pos(self):
        return self.pos
        
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def get_down(self):
        return self.down
    
    def get_up(self):
        return self.up
    
    def get_hints(self):
        return self.hints