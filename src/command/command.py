import re

class Command:
    def __init__(self,dofhandler):
        self.dofhandler = dofhandler
        self.cmd_valid = ["help","goto"]
        
    def help(self):
        res = "command list :\n"
        for cmd in self.cmd_valid:
            res += f"  - {cmd} \n"
        return res
        
    def execute(self,inp):
        res = re.fullmatch(r"(\S+)( .*)?",inp)
        if(not res):
            return f"'{inp}' doesn't match the pattern\n"
        cmd = res.group(1)
        arg = res.group(2)
        if(arg):
            arg = arg.strip().split(" ")
        
        if(cmd not in self.cmd_valid):
            return f"'{cmd}' not found\n"
        
        if(cmd == "help"):
            return self.help()
        
        rep = self.dofhandler.execute(cmd,arg)
            
        return rep