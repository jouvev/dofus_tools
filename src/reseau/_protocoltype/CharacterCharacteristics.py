import src.reseau.protocoltypefactory as pf

class CharacterCharacteristics:
    def __init__(self,content):
        self.caraclen = content.readUnsignedShort()
        self.caracid = []
        self.carac = []
        
        for i in range(self.caraclen):
            self.caracid.append(content.readUnsignedShort())
            self.carac.append(pf.ProtocolTypeFactory.get_instance_id(self.caracid[i],content))
    
    def resume(self):
        for c in self.carac:
            c.resume()