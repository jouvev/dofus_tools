from src.reseau.custominput import CustomInput
from src.dofus.world import World

path = "C:\\Users\\vincent\\AppData\\Local\\Ankama\\zaap\\dofus\\content\\maps\\world-graph.binary"

f = open(path,"rb")
a = f.read()
nbbit = 4*len(a.hex())

data = CustomInput(bin(int(a.hex(),16))[2:].zfill(nbbit))
edgeCount = data.readInt()
print("nb edge",edgeCount)

w = World()

set_type = set()
set_direction = set()
set_id = set()
set_skill = set()

for i in range(edgeCount):
    print(f"{i+1}/{edgeCount}")
    mapid1, zone1  = data.readDouble(),data.readInt()
    mapid2, zone2  = data.readDouble(),data.readInt()
    transitionCount = data.readInt()
    for j in range(transitionCount):
        direction = data.readByte()
        type = data.readByte()
        skill = data.readInt()
        criterion = data.readUTFBytes(data.readInt())
        transitionMapId = data.readDouble()
        cell = data.readInt()
        id = data.readDouble()
    
    set_type.add(type)
    set_direction.add(direction)
    set_id.add(id)
    set_skill.add(skill)
    w.add_edge((mapid1,zone1),(mapid2,zone2),direction,cell,type)

#liste des maps à changer
w.add_edge((185862149,1),(185862148,1),6,6,8)#-2,-4 => -2,-5
w.add_edge((70778880,1),(185863682,1),2,430,1)#1,-8 => 1,-7 changement de type et cell
w.add_edge((95420418.0,1),(90703872.0,1),0,335,2)#14,26 => 15,26 changement de cell
   
print("save")
w.serialize()
"""print("type : ",set_type)
print("direction : ",set_direction)
print("id : ",set_id)
print("skill : ",set_skill)"""

    


