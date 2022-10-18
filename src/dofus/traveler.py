from threading import Thread,Condition
from src.dofus.world import World
import time 
import random


class Traveler(Thread):
    def __init__(self, dofus, src, dest):
        Thread.__init__(self)
        w = World()
        w.deserialize()
        path = w.findpath(src, dest)
        if(not path):
            self.a = []
        else:
            self.a = path[1]
        self.dofus = dofus
        self.condition = Condition()
        
    def next_action(self):
        with self.condition:
            self.condition.notify()
        
    def run(self):
        for a in self.a:
            self.dofus.change_map(a)
            with self.condition:
                self.condition.wait()
            time.sleep(random.random()*0.3+0.5) 
            
        
    