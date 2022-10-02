import re
path = "C:\\Users\\vincent\\Desktop\\dofus source\\scripts_2\\com\\ankamagames\\dofus\\network\\messages\\game\\chat\\ChatClientPrivateMessage.as"

with open(path) as f:
    lines = f.readlines()
    
res = ""
    
for l in lines:
    #rules
    lpython = re.sub("\s*}\s*","",l)
    lpython = re.sub("\s*{\s*","",lpython)
    lpython = re.sub(r"^   (.*)",r"\1",lpython)
    lpython = re.sub(r"(.*);$",r"\1",lpython)
    lpython = re.sub(r" ?: ?[a-zA-Z]+",r"",lpython)
    lpython = re.sub(r"package .*","",lpython)
    lpython = re.sub(r"import (.*)",r"",lpython)
    lpython = re.sub(r"(\s*)(override )?(public|private) function ([a-zA-Z_]+)\(([a-zA-Z,]+)\)",r"\1def \4(self,\5) :",lpython)
    lpython = re.sub(r"this.",r"self.",lpython)
    lpython = re.sub(r"super\(([^\)]*)\)",r"super().__init__(\1)",lpython)
    lpython = re.sub(r"super\.",r"super().",lpython)
    lpython = re.sub(r"var ",r"",lpython)
    lpython = re.sub(r" implements (.*)",r"",lpython)
    lpython = re.sub(r"public class ([a-zA-Z]+) (extends) ([a-zA-Z]+)",r"class \1(\3):",lpython)
    lpython = re.sub(r"public class ([a-zA-Z]+)",r"class \1:",lpython)
    lpython = re.sub(r"new",r"",lpython)
    
    res += lpython
    
res = res.strip()

dectectend = False
for i,l in enumerate(res.split("\n")):
    if(dectectend and "def" in l):
        f = i
        break
    if(not dectectend and "def deserializeAs_" in l):
        d = i
        dectectend=True
     
res = '\n'.join(res.split("\n")[0:1]+res.split("\n")[d:f])
res = re.sub(r"def deserializeAs_([a-zA-Z]+)\(self,reader\):",r"def deserializeAs_\1(self,reader):",res)

res = re.sub(r"def deserializeAs_([a-zA-Z]+)\(([a-zA-Z,]+)\) ?:",r"def __init__(\2):",res)
res = re.sub(r"super().deserialize",r"super().__init__",res)


print(res.strip())
        