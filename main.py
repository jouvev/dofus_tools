from interface.dofus_overlay import DofusOverlay
from src.listener import Listener
from src.dofusmanager import DofusManager
from reseau.sniffer import PacketSniffer

man = DofusManager()
handler = man.dofus_handler
interface = DofusOverlay(handler.get_name_in_order())

listener = Listener(man,interface)
sniff = PacketSniffer(interface,man)

listener.start()
man.start()
sniff.start()
interface.mainloop()

print('wait end')
listener.join()
man.join()
sniff.join()

print("END")