from src.dofus.dofushandler import DofusHandler
import win32gui

dh = DofusHandler()
dh.start()
d = dh.dofus[0]
x,y = win32gui.ScreenToClient(d.hwnd,(1100,234))
