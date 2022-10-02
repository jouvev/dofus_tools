from dofus.dofushandler import DofusHandler
from interface.dofus_overlay import DofusOverlay
from dofus.dofusmanager import DofusManager
from interface.listener import Listener
from reseau.sniffer import PacketSniffer
import json 

config = json.load(open("script/config.json"))

dh = DofusHandler()
dh.start()
dm = DofusManager(config,dh)
dm.start()

interface = DofusOverlay(config,dh.dofus_hwnd,dh.get_names())
Listener(dm,interface).start()
sniff = PacketSniffer(dm)
sniff.start()

dh.add_observer("update_hwnd",lambda order,order_name : interface.update_order(order,order_name))

interface.mainloop()