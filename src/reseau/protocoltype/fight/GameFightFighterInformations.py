from reseau.protocoltype.fight.GameContextActorInformations import GameContextActorInformations
import reseau.protocoltypefactory as pf
from reseau.protocoltype.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation

class GameFightFighterInformations(GameContextActorInformations):
    def __init__(self,content):
        super().__init__(content)
        self.spawnInfo = GameContextBasicSpawnInformation(content)
        self.wave = content.readByte()
        id3 = content.readUnsignedShort()
        self.stats = pf.ProtocolTypeFactory.get_instance_id(id3,content)
        
        self.previouslen = content.readUnsignedShort()
        self.previous = []
        for i in range(self.previouslen):
            self.previous.append(content.readUnsignedShort())
        
    def resume(self):
        super().resume()
        self.spawnInfo.resume()
        print("wave",self.wave)
        self.stats.resume()
        for p in self.previous:
            print("previous",p)