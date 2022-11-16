import logging
import win32process
import win32gui
import win32api
import win32con
import psutil
import time
import random
import win32com.client
import pythoncom
from concurrent.futures import ThreadPoolExecutor
from src.reseau.dofussniffer import PacketSniffer
from src.reseau.MessagesFactory import MessagesFactory
from src.tools.observer import Observer
from src.dofus.mapposition import MapPosition
from src.dofus.traveler import Traveler
from src.chasse.chasse import Chasse
from src.dofus.cell import get_cursor_pos, get_cursor_pos_to_change_map
import pywintypes
from threading import Condition,Lock

class Dofus(Observer):
    def __init__(self,hwnd):
        super().__init__(["fight","newmap","newmapinfos"])
        self.hwnd = hwnd
        _,self.pid = win32process.GetWindowThreadProcessId(hwnd)
        self.set_name()
        self.set_port()
        self.currentmapid = None
        self.cellid = None
        self.travel = None
        self.chasseObject = None
        self.travelCondition = Condition()
        self.travelerLock = Lock()
        self.dofusExec = ThreadPoolExecutor(max_workers=1)
        self.dofusSnifferThread = ThreadPoolExecutor(max_workers=1)
        
        self.dofusSniffer = None
        if not (self.port == ""):
            self.sniffer_attach()
            
        self.gamesynchro = None
        self.turnlist = None
        
        self.click_confirm = False
        
    def sniffer_async(self,action,*args):
        f = self.dofusSnifferThread.submit(action,self,*args)
        f.add_done_callback(self.res_print)
        
    def do_async_action(self,action,*args):
        f = self.dofusExec.submit(action,self,*args)
        f.add_done_callback(self.res_print)
        
    def res_print(self,f):
        res = f.result()
        excep = f.exception()
        if(excep is not None):
            raise excep
        elif(res is not None):
            logging.info(f"{res}")
        
    def stop(self):
        if( self.dofusSniffer is not None):
            self.dofusSniffer.stop()
            self.dofusSniffer.join()
            logging.info(f"{self.name} : sniffer stopped")
            self.dofusSniffer = None
                
        self.stoptravel()
        
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
            
    def change_map_by_cellid(self,cellid,direction,type,delay=True):
        x,y = get_cursor_pos_to_change_map(int(cellid),int(direction),int(type))
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
        if(self.dofusSniffer is None and self.port != ""):
            self.dofusSniffer = PacketSniffer(self)
            logging.info(f"sniffer create to {self.name}")
            self.dofusSniffer.start()
        elif(self.dofusSniffer is not None and self.port != ""):
            logging.info(f"{self.name} : sniffer update to {self.port}")
            self.dofusSniffer.change_port(self.port)
        
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
        
        if("GameFightSynchronizeMessage".lower() == msgname.lower() or "GameFightTurnListMessage".lower() == msgname.lower()):
            self.sniffer_async(Dofus.fight,msgname,p)
        elif("MapComplementaryInformationsDataMessage".lower() == msgname.lower()):
            self.sniffer_async(Dofus.mapinfos,msgname,p)
        elif("CurrentMapMessage".lower() == msgname.lower()):
            self.sniffer_async(Dofus.newmapid,msgname,p)
        elif("TreasureHuntMessage".lower() == msgname.lower()):
            self.sniffer_async(Dofus.chasse,msgname,p)
            
    def endchasse(self):
        if(self.chasseObject):
            self.chasseObject = None
            
    def chasse(self,msgname,p):
        msg = MessagesFactory.get_instance_id(p.packetid,p.get_content())
        if(self.chasseObject is None):
            self.chasseObject = Chasse(self)
            self.chasseObject.start()
        self.chasseObject.read_chasse_msg(msg)
        
    def newmapid(self,msgname,p):
        inst = MessagesFactory.get_instance_id(p.packetid,p.get_content())
        self.currentmapid = inst.mapId
        self.notify("newmap",inst)
        if(self.chasseObject):
            self.chasseObject.newcurrentmap(self.currentmapid)
            
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
        self.notify("newmapinfos",inst)
    
    def open(self):
        try :
            pythoncom.CoInitialize()
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('')
            win32gui.ShowWindow(self.hwnd,3)
            win32gui.SetForegroundWindow(self.hwnd)
        except pywintypes.error as e :
            logging.error(f"Error when open {self.name} {e}")
            return
            
        
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
        with self.travelerLock:
            self.remove_observer("newmapinfos",self.travel.next_action)
            self.travel = None
            logging.info(f"{self.name}: travel finished")
            with self.travelCondition:
                self.travelCondition.notify()
        
    def stoptravel(self):
        with self.travelerLock:
            if(self.travel):
                self.travel.interrupt()
                return f"{self.name} : travel interrupted"
            return f"{self.name} : no travel to stop"
        
    def goto(self,x,y):
        self.travelerLock.acquire()
        if(self.travel is not None):
            logging.info(f'already travelling, wait for interruption')
            self.travel.interrupt()
            with self.travelCondition:
                self.travelerLock.release()
                self.travelCondition.wait()
                self.travelerLock.acquire()
            

        logging.info(f"goto {x},{y}")
        if(self.currentmapid is None or self.cellid is None):
            logging.error(f"{self.name} : no current map infos")
            self.travelerLock.release()
            return "no current map infos"
        src = self.currentmapid,MapPosition.get_linkedzone(self.currentmapid,self.cellid)
        dst = (int(x),int(y))
        self.travel = Traveler(self,src,dst)
        self.add_observer("newmapinfos",self.travel.next_action)
        time.sleep(random.random())#pour pas que que tous les perso partent en meme temps
        self.travel.start()
        self.travelerLock.release()
        return f"{self.name} : travel from {MapPosition.get_pos(src[0])} to {dst}"
    
    def press_key(self,key):
        win32gui.SendMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)
        win32gui.SendMessage(self.hwnd, win32con.WM_KEYUP, key, 0)
    
    def press_enter(self):
        win32gui.SendMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        
    def write(self,text):
        for c in text:
            win32gui.SendMessage(self.hwnd, win32con.WM_CHAR, ord(c), 0)
            
    def invite(self,names):
        for n in names:
            realx,realy = win32gui.ScreenToClient(self.hwnd,(116,1028))
            self.click(realx,realy,False)
            self.write(f"/invite {n}")
            self.press_enter()
            time.sleep(0.1)
        
    def zaap(self,nom):
        #verif si on est deja dans le havre sac
        if(self.currentmapid != 162791424):
            #si pas dans le havre sac, on va dans le havre sac
            self.press_key(0x48)
            time.sleep(1.5)
        #click zaap
        realx,realy = win32gui.ScreenToClient(self.hwnd,(565,433))
        self.click(realx,realy,False)
        time.sleep(1)
        #ecrire le nom
        self.write(nom)
        self.press_key(0xFF)#met à jour la liste des zaaps
        time.sleep(0.5)
        if(nom.lower() == "sufokia"):
            realx,realy = win32gui.ScreenToClient(self.hwnd,(873,365))
            self.click(realx,realy,False)
            time.sleep(0.3)
        self.press_enter()
        return f"{self.name} : zaap to {nom} done"
        