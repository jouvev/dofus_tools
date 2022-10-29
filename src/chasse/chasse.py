from threading import Thread, Condition
from src.dofus.mapposition import MapPosition
from src.chasse.worldhint import WorldHint
from src.dofus.direction import Direction
from src.chasse.phorreursearcher import PhorreurSeacher
import pickle
import logging
import json
import win32gui 
import time

class Chasse(Thread):
    def __init__(self, dofus):
        Thread.__init__(self,name="Chasse")
        try :
            with open('src/chasse/flagpos.pkl','rb') as f : 
                self.xflag , self.yflag = pickle.load(f)
        except :
            self.set_flag_pos(309,670)
        self.dofus = dofus
        self.hintBD = WorldHint.get_instance()
        with open("ressources/poi.json",encoding="utf-8") as file :
            self.poitoindice = json.load(file)
        self.endCond = Condition()
        self.startCond = Condition()
        self.search = None
        self.startmap = -1000.0
        self.xdst,self.ydst = None,None
        
    def set_flag_pos(self,xflag,yflag):
        logging.info("set flag position to {} {}".format(xflag,yflag))
        self.xflag = xflag
        self.yflag = yflag
        with open('src/chasse/flagpos.pkl','wb') as f : 
            pickle.dump((self.xflag , self.yflag),f)
    
    def read_chasse_msg(self,msg):
        self.listindice = msg.knownStepsList
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
        self.checkpoint = msg.checkPointCurrent
        
        if(self.checkpoint != 0 or len(self.listindice) > 1):
            #attention si phorreur
            if("Phorreur".lower() in self.indice.lower()):
                logging.info(f"Chasse: Phorreur npcid {self.npcid}")
                self.search = PhorreurSeacher(self.npcid,self,self.direction)
                self.search.start()
                return 
            #sinon goto indice
            if(self.indicevalide > 0):
                xsrc,ysrc = MapPosition.get_pos(msg.flags[-1].mapId)
            else:
                xsrc,ysrc = MapPosition.get_pos(msg.startMapId)
            try:
                self.xdst,self.ydst = self.get_pos_indice(xsrc,ysrc,self.indice,self.direction)
            except :
                logging.warning(f"Chasse:{self.dofus.name}: indice not found")
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
            except :
                logging.warning(f"Chasse:{self.dofus.name}: indice not found")
                return
        logging.info("Chasse: {} {} at pos {} {}".format(self.indice,self.direction,self.xdst,self.ydst))
            
    def get_pos_indice(self,xsrc,ysrc,indice,direction):
        return self.hintBD.get_hint(xsrc,ysrc,direction,indice)
    
    def newcurrentmap(self,mapid):
        currx,curry = MapPosition.get_pos(mapid)
        if(mapid == self.startmap and self.checkpoint == 0 and len(self.listindice) <= 1):
            if("Phorreur".lower() in self.indice.lower()):
                logging.info(f"Chasse: Phorreur npcid {self.npcid}")
                self.search = PhorreurSeacher(self.npcid,self,self.direction)
                self.search.start()
            else:
                if self.xdst and self.ydst:
                    self.dofus.goto(self.xdst,self.ydst)
            logging.info("Chasse: start map reached")
        if(self.xdst is not None and self.ydst is not None and self.xdst == currx and self.ydst == curry):
            self.dofus.stoptravel()
            self.click_on_flag()
            
    def notify_cond_end(self):
        if(self.search):
            self.search.end = True
        with self.endCond:
            self.endCond.notify()
            
    def click_on_flag(self):
        y = self.yflag + self.indicevalide * 30
        realx,realy = win32gui.ScreenToClient(self.dofus.hwnd,(self.xflag,y))
        time.sleep(0.5)
        self.dofus.click(realx,realy,False)
        logging.info("Chasse: click on flag")
        
    def next_step(self):
        y = self.yflag + self.indicevalide * 30
        realx,realy = win32gui.ScreenToClient(self.dofus.hwnd,(self.xflag-20,y))
        self.dofus.click(realx,realy,False)
        logging.info("Chasse: click on next step")
            
    def run(self):
        with self.endCond:
            self.endCond.wait()
        try :
            self.hintDB.driver.close()
        except :
            pass 
        self.dofus.endchasse()
        logging.info("Chasse: end of chasse")