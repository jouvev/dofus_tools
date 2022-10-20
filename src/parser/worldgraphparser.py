from src.reseau.custominput import CustomInput
from src.dofus.mapposition import MapPosition
from src.dofus.world import World
path = "C:\\Users\\vincent\\AppData\\Local\\Ankama\\zaap\\dofus\\content\\maps\\world-graph.binary"

f = open(path,"rb")
a = f.read()
nbbit = 4*len(a.hex())

data = CustomInput(bin(int(a.hex(),16))[2:].zfill(nbbit))
edgeCount = data.readInt()
print("nb edge",edgeCount)

w = World()

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
    
    w.add_edge((mapid1,zone1),(mapid2,zone2),direction,cell)
    
print("save")
w.serialize()
    


