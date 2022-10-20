from threading import Thread, Condition
import logging
import time

class PhorreurSeacher(Thread):
    def __init__(self,npcid,chasse,direction):
        Thread.__init__(self)
        self.npcid = npcid
        self.direction = direction
        self.chasse = chasse
        self.dofus = chasse.dofus
        self.dofus.add_observer("newmap",self.parse_map)
        self.newMapCond = Condition()
        self.end = False
        self.nbmap = 0
        
    def parse_map(self,msg):
        npcid = -1
        for a in msg.actors:
            try:
                npcid = a.npcId
            except:
                continue
        if(npcid == self.npcid):
            self.gotit()
        with self.newMapCond:
            self.newMapCond.notify()
            
    def gotit(self):
        self.dofus.remove_observer("newmap",self.parse_map)
        logging.info(f"Chasse: got phorreur {self.npcid}, next step")
        time.sleep(1) # attendre fin de chargement avant de cliquer dur le drapeau
        self.chasse.click_on_flag()
        self.end = True
        
    def run(self):
        while not self.end and self.nbmap <= 10:
            self.dofus.change_map(self.direction)
            logging.info(f"Chasse: goto {self.direction}")
            self.nbmap += 1
            with self.newMapCond:
                self.newMapCond.wait()
        
        logging.info(f"Chasse: phorreur {self.npcid} terminated")
        if(self.nbmap > 10):
            logging.info("Chasse: phorreur not found")
            
        