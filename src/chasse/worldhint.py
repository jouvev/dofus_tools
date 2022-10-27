import pickle

class WorldHint:
    def __init__(self):
        self.posToNode = dict()
        
    def get_node(self, pos):
        return self.posToNode[pos]
    
    def add_node(self, maphint):
        self.posToNode[maphint.get_pos()] = maphint
    
    def get_hints(self, pos, direction, hint):
        curr = self.get_node(pos).get_directon(direction)
        for i in range(9):
            if hint in curr.get_hints():
                return curr.get_pos()
            curr = curr.get_directon(direction)
        return None
    
    def add_hint(self,pos,hint):
        self.get_node(pos).add_hint(hint)
        
    def add_map_direction(self,pos,direction,maphint):
        self.get_node(pos).add_map_direction(direction, maphint)
        
    def sereliaze(self):
        with open("ressources\\worldhint.pkl", "wb") as f:
            pickle.dump(self.posToNode, f)

    def deserialize(self):
        with open("ressources\\worldhint.pkl", "rb") as f:
            self.posToNode = pickle.load(f)