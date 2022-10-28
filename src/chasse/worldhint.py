import pickle

class WorldHint:
    __instance = None
    
    def __init__(self):
        self.posToNode = dict()
    
    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            cls.__instance = WorldHint()
            cls.__instance.deserialize()
        return cls.__instance
        
    def get_node(self, pos):
        return self.posToNode[pos]
    
    def add_node(self, maphint):
        self.posToNode[maphint.get_pos()] = maphint
    
    def get_hint(self, posx, posy, direction, hint):
        pos = (posx, posy)
        curr_pos = self.get_node(pos).get_directon(direction)
        curr = self.posToNode[curr_pos]
        for i in range(10):
            if hint in curr.get_hints():
                return curr.get_pos()
            curr_pos = curr.get_directon(direction)
            curr = self.posToNode[curr_pos]
        raise RuntimeError("Hint not found")
    
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