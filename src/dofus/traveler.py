from threading import Thread,Condition
from src.dofus.world import World
import time 
import random
from src.tools.observer import Observer


class Traveler(Thread,Observer):
    def __init__(self, dofus, src, dest):
        Thread.__init__(self)
        Observer.__init__(self, ["finished"])
        w = World()
        w.deserialize()
        path = w.findpath(src, dest)
        if(not path):
            self.a = []
        else:
            self.a = path[1]
        self.dofus = dofus
        self.condition = Condition()
        
    def interrupt(self):
        self.stopped = True
        
    def next_action(self,msg):
        with self.condition:
            self.condition.notify()
        
    def run(self):
        self.stopped = False
        self.add_observer("finished",self.dofus.travel_finished)
        for i,a in enumerate(self.a):
            self.dofus.change_map(a,delay=False)
            with self.condition:
                self.condition.wait()
            if(i != len(self.a)-1):
                time.sleep(random.random()*0.3+1)
            if(self.stopped):
                break
        self.notify("finished")
            
        
    