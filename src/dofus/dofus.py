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
from src.dofus.map import Map

class Dofus(Observer):
    def __init__(self,hwnd):
        super().__init__(["fight"])
        self.hwnd = hwnd
        _,self.pid = win32process.GetWindowThreadProcessId(hwnd)
        self.set_name()
        self.set_port()
        self.currentpos = None
        
        self.dofusSniffer = None
        if not (self.port == ""):
            self.dofusSniffer = self.sniffer_attach()
            
        self.gamesynchro = None
        self.turnlist = None
            
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
            
    def change_map(self,direction):
        if(direction == "left"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(280,426))
            self.click(realx,realy)
        elif(direction == "right"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(1617,614))
            self.click(realx,realy)
        elif(direction == "down"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(844,915))
            self.click(realx,realy)
        elif(direction == "up"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(866,28))
            self.click(realx,realy)
            
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
        logging.info(f"sniffer create to {self.name}")
        if(self.dofusSniffer is not None):
            self.dofusSniffer.stop()
            self.dofusSniffer.join()
        if(self.port != ""):
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
            logging.info(f"{self.name} : fight started")
            id_hwnd = dict()
            for f in self.gamesynchro.fighters:
                try:
                    hwnd = self.handler.get_hwnd_by_name(f.name)
                except :
                    continue
                id_hwnd[f.contextualId] = hwnd
                
            orderlist = [id_hwnd[conid] for conid in self.turnlist.ids if conid in id_hwnd]
            self.notify("fight",orderlist)
            self.gamesynchro = None
            self.turnlist = None
            
    def packet_received(self,p):
        msgname = MessagesFactory.id_class[str(p.packetid)].__name__
        logging.info(f"{self.name} received {msgname}")
        
        if("GameFightSynchronizeMessage".lower() in msgname.lower() or "GameFightTurnListMessage".lower() in msgname.lower()):
            self.fight(msgname,p)
        elif("CurrentMapMessage".lower() in msgname.lower()):
            self.currentmap(msgname,p)
        #elif("HuntMessage".lower() in msgname.lower()):
    
            
    def currentmap(self,msgname,p):
        inst = MessagesFactory.get_instance_id(p.packetid,p.get_content())
        self.currentpos = Map.get_pos(inst.mapId)
    
    def open(self):
        win32gui.ShowWindow(self.hwnd,3)
        win32gui.SetForegroundWindow(self.hwnd)
        
    def click(self,x,y,delay=True):
        lParam = win32api.MAKELONG(x, y)
        if(delay):
            time.sleep(random.random())
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, None, lParam)