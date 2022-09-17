import reseau.protocoltypefactory as pf

class GameContextBasicSpawnInformation:
    def __init__(self,content):
        self.teamid = content.readByte()
        self.alive = content.readBoolean()
        id3 = content.readUnsignedShort()
        self.info = pf.ProtocolTypeFactory.get_instance_id(id3,content)
        
    def resume(self):
        print("teamid",self.teamid)
        print("alive",self.alive)
        self.info.resume()