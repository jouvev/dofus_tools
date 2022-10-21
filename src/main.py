from dofus.dofushandler import DofusHandler
from interface.dofus_overlay import DofusOverlay
from dofus.dofusmanager import DofusManager
from interface.listener import Listener
import json 
import time
import logging
import argparse
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--nodebug', action='store_false')
args = parser.parse_args()

if(args.nodebug):
    logging.basicConfig(level=logging.INFO)

config = json.load(open("script/config.json",encoding="utf-8"))

dh = DofusHandler()
dm = DofusManager(config,dh)
interface = DofusOverlay(config,dh.get_hwnds(),dh.get_names(),dm.mode)
listener = Listener(dm,interface)

dh.start()
listener.start()

dm.add_observer("stop",interface.stop)
dm.add_observer("stop",dh.stop)
dm.add_observer("update_mode",interface.update_mode)
dm.add_observer("open_console",interface.open_console)

dh.add_observer("update_hwnd",lambda order,order_name : interface.update_order(order,order_name))

interface.mainloop()

for thread in threading.enumerate(): 
    print(thread.name, "running")