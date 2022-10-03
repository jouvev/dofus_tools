import os 

root_path = "C:\\Users\\vincent\\Desktop\\dofus source\\scripts_2\\com\\ankamagames\\dofus\\network\\types"

for root, dirs, files in os.walk(root_path): 
    path = root.split(os.sep)
    for f in files:
        if(f.endswith(".as")):
            print(os.path.join(*path,f))