import reseau.protocoltypefactory as pf

class GameContextActorPositionInformations:
    def __init__(self,content):
        self.contextualid = content.readDouble()
        self.dispo_id = content.readUnsignedShort()
        
        self.dispo = pf.ProtocolTypeFactory.get_instance_id(self.dispo_id,content)
        
    def resume(self):
        print("contextualid",self.contextualid)
        self.dispo.resume()