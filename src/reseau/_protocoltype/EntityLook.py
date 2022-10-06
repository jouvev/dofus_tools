from src.reseau.protocoltype.SubEntity import SubEntity

class EntityLook:
    def __init__(self,content):
        self.bonesid = content.readVarShort()
        
        self.skinslen = content.readUnsignedShort()
        self.skins = []
        for i in range(self.skinslen):
            self.skins.append(content.readVarShort())
            
        self.indexedcolorslen = content.readUnsignedShort()
        self.indexedcolors = []
        for i in range(self.indexedcolorslen):
            self.indexedcolors.append(content.readInt())
            
        self.scaleslen = content.readUnsignedShort()
        self.scales = []
        for i in range(self.scaleslen):
            self.scales.append(content.readVarShort())
            
        self.subentitieslen = content.readUnsignedShort()
        self.subentities = []
        for i in range(self.subentitieslen):
            self.subentities.append(SubEntity(content))

        
    def resume(self):
        print("bonesid",self.bonesid)
        for s in self.skins:
            print("skins",s)
        for i in self.indexedcolors:
            print("indexedcolors",i)
        for s in self.scales:
            print("scales",s)
        for s in self.subentities:
            s.resume()