import logging
import pickle
from src.dofus.mapposition import MapPosition

class World:
    __instance = None
    
    def __init__(self):
        self.graph = dict()
        self.actions = dict()
    
    @classmethod   
    def get_instance(cls):
        if(cls.__instance == None):
            cls.__instance = World()
            cls.__instance.deserialize()
        return cls.__instance
    
    def add_edge(self,src,dst,direction,cell,type):
        if(src not in self.graph):
            self.graph[src] = []
        self.graph[src].append(dst)
        self.actions[(src,dst)] = (direction,cell,type)
        
    def serialize(self):
        with open( "ressources/worldgraph.pkl", "wb" ) as file :
            pickle.dump(self.graph,file)
        with open( "ressources/worldgraphactions.pkl", "wb" ) as file:
            pickle.dump(self.actions,file)
        
    def deserialize(self):
        with open( "ressources/worldgraph.pkl", "rb" ) as file :
            self.graph = pickle.load(file)
        with open( "ressources/worldgraphactions.pkl", "rb" ) as file:
            self.actions = pickle.load(file)
        
    def __getitem__(self,key):
        return self.graph[key]
    
    def findpath(self,src,dst):
        q = [src]
        pred = dict()
        dejavu = set()
        path = []
        find = False
        
        dejavu.add(q[0])
        #parcour en largeur
        while len(q) > 0:
            cur = q.pop(0)
            if MapPosition.get_pos(cur[0]) == dst:
                find = True
                break
            if cur in self.graph:
                for n in self.graph[cur]:
                    if(n not in dejavu):
                        q.append(n)
                        dejavu.add(n)
                        pred[n] = cur
                        
        if(not find):
            logging.error(f"no path found from {src} to {dst}")
            return [],[]
                        
        #reconstruction du chemin
        while cur != src:
            path.append(cur)
            cur = pred[cur]
        path.append(src)
            
        path.reverse()
        
        #action
        action = []
        for i in range(len(path)-1):
            src = path[i]
            dst = path[i+1]
            a = self.actions[(src,dst)]
            try:
                action.append(a)
            except:
                raise RuntimeError(f"action non reconnu dans pathfinding {[(MapPosition.get_pos(p[0][0]),p[0]) for p in path]}")
                
        return path,action