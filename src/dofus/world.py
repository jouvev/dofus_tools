import logging
import pickle
from src.dofus.mapposition import MapPosition
from src.dofus.direction import Direction

class World:
    def __init__(self):
        self.graph = dict()
        self.actions = dict()
    
    def add_edge(self,src,dst,direction,cell):
        if(src not in self.graph):
            self.graph[src] = []
        self.graph[src].append(dst)
        self.actions[(src,dst)] = (direction,cell)
        
    def serialize(self):
        pickle.dump( self.graph, open( "ressources/worldgraph.pkl", "wb" ) )
        pickle.dump( self.actions, open( "ressources/worldgraphactions.pkl", "wb" ) )
        
    def deserialize(self):
        self.graph = pickle.load( open( "ressources/worldgraph.pkl", "rb" ) )
        self.actions = pickle.load( open( "ressources/worldgraphactions.pkl", "rb" ) )
        
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
            if cur == dst:
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
            return None
                        
        #reconstruction du chemin
        cur = dst
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
            a = self.actions[(src,dst)][0]
            try:
                action.append(Direction(a).name)
            except:
                raise RuntimeError(f"action non reconnu dans pathfinding {[(MapPosition.get_pos(p[0][0]),p[0]) for p in path]}")
                
        return path,action