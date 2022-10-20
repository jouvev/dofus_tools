from threading import Thread, Condition
from src.dofus.mapposition import MapPosition
from src.chasse.dofusdb import DofusDB
from src.dofus.direction import Direction
import logging
import json
import win32gui 

class Chasse(Thread):
    def __init__(self, dofus):
        Thread.__init__(self)
        self.dofus = dofus
        self.ddb = DofusDB()
        self.poitoindice = json.load(open("ressources/poi.json",encoding="utf-8"))
        self.endCond = Condition()
        self.startCond = Condition()
        self.startmap = -1000.0
        
    def read_chasse_msg(self,msg):
        listindice = msg.knownStepsList
        self.indicevalide = len(msg.flags)
        totalstep = msg.totalStepCount
        if(totalstep == 0):
            self.notify_cond_end()
            return 
        if(totalstep == self.indicevalide):
            self.next_step()
            logging.info("Chasse: end of this step chasse")
            return
        
        try:
            indice = self.poitoindice[str(msg.knownStepsList[-1].poiLabelId)]
        except:
            indice = "Phorreur"
            logging.info(f"Chasse: Phorreur npcid {msg.knownStepsList[-1].npcId}")
        
        dir = Direction(msg.knownStepsList[-1].direction).name
        checkpoint = msg.checkPointCurrent
        
        if(checkpoint != 0 or len(listindice) > 1):
            #attention si phorreur
            if("Phorreur".lower() in indice.lower()):
                return 
            #sinon goto indice
            xsrc,ysrc = MapPosition.get_pos(self.dofus.currentmapid)
            try:
                self.xdst,self.ydst = self.get_pos_indice(xsrc,ysrc,indice,dir)
            except KeyError:
                logging.info("Chasse: indice not found")
                return 
            self.dofus.goto(self.xdst,self.ydst)
        else :
            self.startmap = msg.startMapId
            self.xstart,self.ystart = MapPosition.get_pos(self.startmap)
            logging.info("Chasse: start position {} {}".format(self.xstart,self.ystart))
            try:
                self.xdst,self.ydst = self.get_pos_indice(self.xstart,self.ystart,indice,dir)
            except KeyError:
                logging.info("Chasse: indice not found")
                return
        logging.info("Chasse: {} {} at pos {} {}".format(indice,dir,self.xdst,self.ydst))
            
    def get_pos_indice(self,xsrc,ysrc,indice,dir):
        indiceslist = self.ddb.get_hints(xsrc,ysrc,dir)
        xdst,ydst = indiceslist[indice]
        return xdst,ydst
    
    def newcurrentmap(self,mapid):
        if(mapid == self.startmap):
            self.notify_cond_start()
            logging.info("Chasse: start map reached")
    
    def notify_cond_start(self):
        with self.startCond:
            self.startCond.notify()
            
    def notify_cond_end(self):
        with self.endCond:
            self.endCond.notify()
            self.ddb.driver.close()
            
    def endtravel(self):
        y = 670 + self.indicevalide * 30
        realx,realy = win32gui.ScreenToClient(self.dofus.hwnd,(309,y))
        self.dofus.click(realx,realy,False)
        logging.info("Chasse: click on flag")
        
    def next_step(self):
        y = 670 + self.indicevalide * 30
        realx,realy = win32gui.ScreenToClient(self.dofus.hwnd,(293,y))
        self.dofus.click(realx,realy,False)
        logging.info("Chasse: click on next step")
            
    def run(self):
        with self.startCond:
            self.startCond.wait()
        self.dofus.goto(self.xdst,self.ydst)
        with self.endCond:
            self.endCond.wait()
        logging.info("Chasse: end of chasse")