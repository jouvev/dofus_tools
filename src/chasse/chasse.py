from threading import Thread, Condition
from src.dofus.mapposition import MapPosition
from src.chasse.dofusdb import DofusDB
from src.dofus.direction import Direction
from src.chasse.phorreursearcher import PhorreurSeacher
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
        self.xdst,self.ydst = None,None
        
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
            self.indice = self.poitoindice[str(msg.knownStepsList[-1].poiLabelId)]
        except:
            self.indice = "Phorreur"
            self.npcid = msg.knownStepsList[-1].npcId
        
        self.direction = Direction(msg.knownStepsList[-1].direction).name
        checkpoint = msg.checkPointCurrent
        
        if(checkpoint != 0 or len(listindice) > 1):
            #attention si phorreur
            if("Phorreur".lower() in self.indice.lower()):
                logging.info(f"Chasse: Phorreur npcid {self.npcid}")
                search = PhorreurSeacher(self.npcid,self,self.direction)
                search.start()
                return 
            #sinon goto indice
            if(self.indicevalide > 0):
                xsrc,ysrc = MapPosition.get_pos(msg.flags[-1].mapId)
            else:
                xsrc,ysrc = MapPosition.get_pos(msg.startMapId)
            try:
                self.xdst,self.ydst = self.get_pos_indice(xsrc,ysrc,self.indice,self.direction)
            except KeyError:
                logging.info("Chasse: indice not found")
                return 
            self.dofus.goto(self.xdst,self.ydst)
        else :
            self.startmap = msg.startMapId
            self.xstart,self.ystart = MapPosition.get_pos(self.startmap)
            logging.info("Chasse: start position {} {}".format(self.xstart,self.ystart))
            if("Phorreur".lower() in self.indice.lower()):
                return
            try:
                self.xdst,self.ydst = self.get_pos_indice(self.xstart,self.ystart,self.indice,self.direction)
            except KeyError:
                logging.info("Chasse: indice not found")
                return
        logging.info("Chasse: {} {} at pos {} {}".format(self.indice,self.direction,self.xdst,self.ydst))
            
    def get_pos_indice(self,xsrc,ysrc,indice,direction):
        indiceslist = self.ddb.get_hints(xsrc,ysrc,direction)
        xdst,ydst = indiceslist[indice]
        return xdst,ydst
    
    def newcurrentmap(self,mapid):
        currx,curry = MapPosition.get_pos(mapid)
        if(mapid == self.startmap):
            if("Phorreur".lower() in self.indice.lower()):
                logging.info(f"Chasse: Phorreur npcid {self.npcid}")
                search = PhorreurSeacher(self.npcid,self,self.direction)
                search.start()
            else:
                self.dofus.goto(self.xdst,self.ydst)
            logging.info("Chasse: start map reached")
        if(self.xdst and self.ydst and self.xdst == currx and self.ydst == curry):
            self.dofus.stoptravel()
            self.click_on_flag()
            
    def notify_cond_end(self):
        with self.endCond:
            self.endCond.notify()
            
    def click_on_flag(self):
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
        with self.endCond:
            self.endCond.wait()
        self.ddb.driver.close()
        self.dofus.endchasse()
        logging.info("Chasse: end of chasse")