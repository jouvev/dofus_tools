from interface.dofus_overlay import DofusOverlay
from src.listener import Listener
from src.dofusmanager import DofusManager

man = DofusManager()
handler = man.dofus_handler
interface = DofusOverlay(handler.get_name_in_order())

listener = Listener(man,interface)

interface.mainloop()
listener.start()
man.run()