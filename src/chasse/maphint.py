from src.dofus.direction import Direction

class MapHint:
    def __init__(self,pos):
        self.pos = pos
        self.right = None
        self.left = None
        self.down = None
        self.up = None
        self.hints = []
        
    def add_map_direction(self, direction, pos):
        if (Direction(direction) == Direction.right):
            self.right = pos
        elif (Direction(direction) == Direction.left):
            self.left = pos
        elif (Direction(direction) == Direction.down):
            self.down = pos
        elif(Direction(direction) == Direction.up):
            self.up = pos
        
    def add_hint(self, hint):
        self.hints.append(hint)
        
    def get_directon(self,direction):
        if (direction == 'right'):
            return self.right
        elif (direction == 'left'):
            return self.left
        elif (direction == 'down'):
            return self.down
        elif(direction == 'up'):
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