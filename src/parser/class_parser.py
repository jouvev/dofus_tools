import re
path = "C:\\Users\\vincent\\Desktop\\dofus source\\scripts_2\\com\\ankamagames\\dofus\\network\\messages\\game\\chat\\ChatClientPrivateMessage.as"

with open(path) as f:
    lines = f.readlines()
    
class_python = ""
nb_tab = 0
imports = []

for i in range(len(lines)):
    l = lines[i][:-2].strip()
    if 'class' in l:
        name, parent = "", ""
        mot = l.split(' ')
        i = mot.index('class')
        name = mot[i+1]
        if 'extends' in l:
            i = mot.index('extends')
            parent = mot[i+1]
        if parent != "":
            class_python = "class " + name + "(" + parent + "):\n"
        else:
            class_python = "class " + name + ":\n"
        nb_tab = 1
        class_python += "\t"*nb_tab + "def __init__(self,content):\n"
        
    if l.startswith("public function deserializeAs_"):
        
        while (i+1 < len(lines) and lines[i+1].strip() != "}"):
            i+=1
            l = lines[i][:-2].strip()
            if (l.startswith("super.deserialize")):
                class_python += "\t"*(nb_tab+1) + "super().__init__(content)\n"
            res = re.findall(l)
            if(res):
                
print(class_python)

def function():
    pass

def boucle_for():
    pass
        