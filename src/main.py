from dofus.dofushandler import DofusHandler
from interface.dofus_overlay import DofusOverlay
from dofus.dofusmanager import DofusManager
from interface.listener import Listener
from src.reseau.sniffer import PacketSniffer
from src.reseau.requestsniffer import RequestSniffer
import json 

config = json.load(open("script/config.json"))

dh = DofusHandler()
dh.start()
dm = DofusManager(config,dh)

interface = DofusOverlay(config,dh.get_hwnds(),dh.get_names())
Listener(dm,interface).start()
sniff = PacketSniffer(dm)
sniff.start()
reqsniff = RequestSniffer(dm)
reqsniff.start()

dm.add_observer("stop",interface.stop)
dm.add_observer("stop",sniff.stop)
dm.add_observer("stop",dh.stop)
dm.add_observer("stop",reqsniff.stop)

dh.add_observer("update_hwnd",lambda order,order_name : interface.update_order(order,order_name))

interface.mainloop()

dh.join()
sniff.join() 