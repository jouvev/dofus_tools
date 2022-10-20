import logging
import pickle
from src.dofus.mapposition import MapPosition

class World:
    def __init__(self):
        self.graph = dict()
    
    def add_edge(self,src,dst):
        if(src not in self.graph):
            self.graph[src] = []
        self.graph[src].append(dst)
        
    def serialize(self):
        pickle.dump( self.graph, open( "ressources/worldgraph.pkl", "wb" ) )
        
    def deserialize(self):
        self.graph = pickle.load( open( "ressources/worldgraph.pkl", "rb" ) )
        
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
            posxdep,posydep = MapPosition.get_pos(path[i][0]) 
            posxdest,posydest = MapPosition.get_pos(path[i+1][0])
            dx = posxdest - posxdep
            dy = posydest - posydep
            if(dx == 1 and dy == 0):
                action.append("right")
            elif(dx == -1 and dy == 0):
                action.append("left")
            elif(dx == 0 and dy == 1):
                action.append("down")
            elif(dx == 0 and dy == -1):
                action.append("up")
            else:
                raise RuntimeError(f"action non reconnu dans pathfinding ({posxdep},{posydep}),({posxdest},{posydest}) {[(MapPosition.get_pos(p[0]),p) for p in path]}")
                
        return path,action