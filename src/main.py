from interface.dofus_overlay import DofusOverlay
from src.listener import Listener
from src.dofusmanager import DofusManager
from reseau.sniffer import PacketSniffer
import json

config = json.load(open("script/config.json"))

man = DofusManager(config)
handler = man.dofus_handler
interface = DofusOverlay(config,handler.get_name_in_order())

listener = Listener(man,interface)
sniff = PacketSniffer(interface,man)

listener.start()
man.start()
sniff.start()
interface.mainloop()

listener.join()
man.join()
sniff.join()

print("END")