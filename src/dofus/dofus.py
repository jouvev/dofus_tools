import logging
import win32process
import win32gui
import win32api
import win32con
import psutil
import time
import random
from src.reseau.dofussniffer import PacketSniffer
from src.reseau.MessagesFactory import MessagesFactory
from src.tools.observer import Observer
from src.dofus.mapposition import MapPosition
from src.dofus.traveler import Traveler
from src.chasse.chasse import Chasse
from src.dofus.cell import get_cursor_pos, get_cursor_pos_to_change_map

class Dofus(Observer):
    def __init__(self,hwnd):
        super().__init__(["fight","newmap"])
        self.hwnd = hwnd
        _,self.pid = win32process.GetWindowThreadProcessId(hwnd)
        self.set_name()
        self.set_port()
        self.currentmapid = None
        self.cellid = None
        self.travel = None
        self.chasseObject = None
        
        self.dofusSniffer = None
        if not (self.port == ""):
            self.sniffer_attach()
            
        self.gamesynchro = None
        self.turnlist = None
        
    def stop(self):
        if( self.dofusSniffer is not None):
            logging.info(f"{self.name} : stop sniffer")
            self.dofusSniffer.stop()
            self.dofusSniffer.join()
            self.dofusSniffer = None
        if(self.travel):
            logging.info(f"{self.name} : stop travel")
            self.travel.interrupt()
        if(self.chasseObject):
            logging.info(f"{self.name} : stop chasse")
            self.chasseObject.notify_cond_end()
             
    def set_name(self):
        name = win32gui.GetWindowText(self.hwnd)
        lname = name.split(" - ")
        if(len(lname) == 1):
            self.name = ""
        else:
            self.name = lname[0]
        
    def set_port(self):
        self.port = ""
        p = psutil.Process(self.pid)
        for conn in p.connections():
            if conn.raddr.port == 5555 :
                self.port = str(conn.laddr.port)
                break
            
    def change_map(self,direction,delay=True):
        if(direction == "left"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(280,426))
            self.click(realx,realy,delay)
        elif(direction == "right"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(1617,614))
            self.click(realx,realy,delay)
        elif(direction == "down"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(844,915))
            self.click(realx,realy,delay)
        elif(direction == "up"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(866,28))
            self.click(realx,realy,delay)
            
    def change_map_by_cellid(self,mapdst,cellid,direction,type,delay=True):
        x,y = get_cursor_pos_to_change_map(self.currentmapid,mapdst,int(cellid),int(direction),int(type))
        realx,realy = win32gui.ScreenToClient(self.hwnd,(x,y))
        self.click(realx,realy,delay)
                       
    def get_infos(self):
        return self.hwnd, self.pid, self.name, self.port
    
    def update_name(self):
        tmp_name = self.name
        self.set_name()
        return tmp_name != self.name
    
    def update_port(self):
        tmp_port = self.port
        self.set_port()
        change = tmp_port != self.port
        if(change):
            logging.debug(f"{self.name} : port change {tmp_port} to {self.port}")
            self.sniffer_attach()
        return change
    
    def sniffer_attach(self):
        if(self.dofusSniffer is not None):
            self.dofusSniffer.stop()
            self.dofusSniffer.join()
            self.dofusSniffer = None
        if(self.port != ""):
            logging.info(f"sniffer create to {self.name}")
            self.dofusSniffer = PacketSniffer(self)
            self.dofusSniffer.start()
        
    def fight(self,msgname,p):
        if("GameFightSynchronizeMessage".lower() in msgname.lower()):            
            content = p.get_content()
            inst = MessagesFactory.get_instance_id(p.packetid,content)
            self.gamesynchro = inst    
        elif("GameFightTurnListMessage".lower() in msgname.lower()):
            content = p.get_content()
            inst = MessagesFactory.get_instance_id(p.packetid,content)
            self.turnlist = inst
        if(self.gamesynchro is not None and self.turnlist is not None):
            idtoname = dict()
            for f in self.gamesynchro.fighters:
                try:
                    idtoname[f.contextualId] = f.name
                except :
                    continue
            orderlist = [idtoname[id] for id in self.turnlist.ids if id in idtoname]
            self.notify("fight",orderlist)
            logging.info(f"{self.name} : fight started {orderlist}")
            self.gamesynchro = None
            self.turnlist = None
            
    def packet_received(self,p):
        msgname = MessagesFactory.id_class[str(p.packetid)].__name__
        logging.debug(f"{self.name} received {msgname}")
        
        if("GameFightSynchronizeMessage".lower() in msgname.lower() or "GameFightTurnListMessage".lower() in msgname.lower()):
            self.fight(msgname,p)
        elif("MapComplementaryInformationsDataMessage".lower() in msgname.lower()):
            self.mapinfos(msgname,p)
        elif("TreasureHuntMessage".lower() in msgname.lower()):
            self.chasse(msgname,p)
            
    def endchasse(self):
        if(self.chasseObject):
            self.chasseObject = None
            
    def chasse(self,msgname,p):
        msg = MessagesFactory.get_instance_id(p.packetid,p.get_content())
        if(self.chasseObject is None):
            self.chasseObject = Chasse(self)
            self.chasseObject.start()
        self.chasseObject.read_chasse_msg(msg)
            
    def mapinfos(self,msgname,p):
        inst = MessagesFactory.get_instance_id(p.packetid,p.get_content())
        
        self.currentmapid = inst.mapId
        
        for a in inst.actors:
            try : 
                name = a.name
            except:
                continue
            if(name == self.name):
                self.cellid = a.disposition.cellId
                break
        self.notify("newmap",inst)
        if(self.chasseObject):
            self.chasseObject.newcurrentmap(self.currentmapid)
    
    def open(self):
        win32gui.ShowWindow(self.hwnd,3)
        win32gui.SetForegroundWindow(self.hwnd)
        
    def click_cell(self,cellid,delay=True):
        x,y = get_cursor_pos(int(cellid))
        realx,realy = win32gui.ScreenToClient(self.hwnd,(x,y))
        self.click(realx,realy,delay)
        
    def click(self,x,y,delay=True):
        lParam = win32api.MAKELONG(x, y)
        if(delay):
            time.sleep(random.random())
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, None, lParam)
        
    def travel_finished(self):
        self.remove_observer("newmap",self.travel.next_action)
        self.travel = None
        logging.info("travel finished")
        
    def stoptravel(self):
        if(self.travel):
            self.travel.interrupt()
            return f"{self.name} : travel interrupted"
        return f"{self.name} : no travel to stop"
        
    def goto(self,x,y):
        logging.info(f"goto {x},{y}")
        src = self.currentmapid,MapPosition.get_linkedzone(self.currentmapid,self.cellid)
        worldsrc = MapPosition.get_worldmap(src[0])
        dst = MapPosition.get_mapid(x,y,worldsrc),1.0
        self.travel = Traveler(self,src,dst)
        self.add_observer("newmap",self.travel.next_action)
        self.travel.start()
        return f"{self.name} : travel from {MapPosition.get_pos(src[0])} to {MapPosition.get_pos(dst[0])}"