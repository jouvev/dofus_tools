from src.dofus.dofushandler import DofusHandler
import win32com.client

dh = DofusHandler()

dh.start()

shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')

while True:
    cmd = input("cmd: ")
    cmd = cmd.strip()
    if(cmd.startswith("zaap")):
        dest = cmd[cmd.index(" ")+1:]
        for d in dh.dofus:
            d.cmd_zaap(dest)