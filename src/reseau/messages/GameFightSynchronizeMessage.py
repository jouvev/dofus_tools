import src.reseau.protocoltypefactory as pf

class GameFightSynchronizeMessage:
    def __init__(self,content):
        self.fighters_len = content.readUnsignedShort()
        self.fighters = []
        self.fighters_id = []
        
        for i in range(self.fighters_len):
            self.fighters_id.append(content.readUnsignedShort())
            self.fighters.append(pf.ProtocolTypeFactory.get_instance_id(self.fighters_id[i],content))
            
    def resume(self):
        print("fighters_len",self.fighters_len)
        for i in range(self.fighters_len):
            print("##############################################")
            print("fighters_id",self.fighters_id[i])
            self.fighters[i].resume()