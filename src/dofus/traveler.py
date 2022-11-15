from threading import Thread,Condition
from src.dofus.world import World
from src.dofus.mapposition import MapPosition
import time 
import logging
from src.tools.observer import Observer

class Traveler(Thread,Observer):
    def __init__(self, dofus, src, dest):
        Thread.__init__(self,name="Traveler")
        Observer.__init__(self, ["finished"])
        self.w = World.get_instance()
        self.dofus = dofus
        self.condition = Condition()
        self.src = src
        self.dest = dest
        
    def interrupt(self):
        self.stopped = True
        self.next_action(None)
        
    def next_action(self,msg):
        with self.condition:
            self.condition.notify()
        
    def run(self):
        try:
            z,path,self.a = self.w.get_path(self.src, self.dest)
            if(z is not None):
                self.dofus.zaap(z['name'])
                with self.condition:
                    self.condition.wait()
            if(path == []):
                return
            dico_path = {m:a for m,a in zip(path[:-1],self.a)}
            dico_path[path[-1]] = "stop"
            self.stopped = False
            self.add_observer("finished",self.dofus.travel_finished)
            
            mapi = (self.dofus.currentmapid,MapPosition.get_linkedzone(self.dofus.currentmapid,self.dofus.cellid))
            while(dico_path[mapi] != "stop" and not self.stopped):
                direction,cell,type = dico_path[mapi]
                logging.debug(f"{self.dofus.name} : {int(direction)} {cell} {type}")
                self.dofus.change_map_by_cellid(cell,direction,type,delay=False)
                with self.condition:
                    self.condition.wait()
                mapi = (self.dofus.currentmapid,MapPosition.get_linkedzone(self.dofus.currentmapid,self.dofus.cellid))
                if (mapi not in dico_path):
                    logging.info("Traveler : out of the way")
                    return
                if(dico_path[mapi] != "stop"):
                    time.sleep(1)
                else:
                    self.stopped = True
                if(self.stopped):
                    break
        except Exception as e:
            logging.error(f"Error in Traveler {e}")
        finally:
            self.notify("finished")
            
        
    