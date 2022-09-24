from src.dofushandler import DofusHandler
from interface.dofus_overlay import DofusOverlay
from src.dofusmanager import DofusManager
from src.listener import Listener
from reseau.sniffer import PacketSniffer
import json 

config = json.load(open("script/config.json"))

dh = DofusHandler()
dh.start()
dm = DofusManager(config,dh)
dm.start()

interface = DofusOverlay(config,dh.dofus_hwnd,dh.get_name_in_order())
Listener(dm,interface).start()
sniff = PacketSniffer(dm)
sniff.start()

dm.add_observer("stop",interface.stop)
dm.add_observer("stop",sniff.stop)
dm.add_observer("stop",dh.stop)

dh.add_observer("update_hwnd",lambda order,order_name : interface.update_order(order,order_name))

interface.mainloop()

dm.join()
dh.join()
sniff.join()