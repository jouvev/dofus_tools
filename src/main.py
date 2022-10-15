from dofus.dofushandler import DofusHandler
from interface.dofus_overlay import DofusOverlay
from dofus.dofusmanager import DofusManager
from interface.listener import Listener
import json 
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--nodebug', action='store_false')
args = parser.parse_args()

if(args.nodebug):
    logging.basicConfig(level=logging.DEBUG)

config = json.load(open("script/config.json"))

dh = DofusHandler()
dm = DofusManager(config,dh)
interface = DofusOverlay(config,dh.get_hwnds(),dh.get_names(),dm.mode)
Listener(dm,interface).start()

dh.start()

dm.add_observer("stop",interface.stop)
dm.add_observer("stop",dh.stop)
dm.add_observer("update_mode",interface.update_mode)

dh.add_observer("update_hwnd",lambda order,order_name : interface.update_order(order,order_name))

interface.mainloop()