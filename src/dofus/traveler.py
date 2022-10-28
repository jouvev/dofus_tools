from threading import Thread,Condition
from src.dofus.world import World
import time 
import random
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
            path = self.w.findpath(self.src, self.dest)
            if(not path):
                return 
            else:
                self.a = path[1]
            self.stopped = False
            self.add_observer("finished",self.dofus.travel_finished)
            
            for i,(direction,cell,type) in enumerate(self.a):
                logging.debug(f"{self.dofus.name} : {int(direction)} {cell} {type}")
                self.dofus.change_map_by_cellid(cell,direction,type,delay=False)
                with self.condition:
                    self.condition.wait()
                if(i != len(self.a)-1):
                    time.sleep(1)
                if(self.stopped):
                    break
        except Exception as e:
            logging.error(f"Error in Traveler {e}")
        finally:
            self.notify("finished")
            
        
    