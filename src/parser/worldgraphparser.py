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
    _1, _2  = data.readDouble(),data.readInt()
    _3, _4  = data.readDouble(),data.readInt()
    transitionCount = data.readInt()
    for j in range(transitionCount):
        _5 = data.readByte()
        _6 = data.readByte()
        _7 = data.readInt()
        _8 = data.readUTFBytes(data.readInt())
        _9 = data.readDouble()
        _10 = data.readInt()
        _11 = data.readDouble()
    
    w.add_edge((_1,_2),(_3,_4))
    
print("save")
w.serialize()
    


