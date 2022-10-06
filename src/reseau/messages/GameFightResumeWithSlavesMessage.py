from src.reseau.messages.GameFightResumeMessage import GameFightResumeMessage
from src.reseau.types.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo

class GameFightResumeWithSlavesMessage(GameFightResumeMessage):
   def __init__(self,input):
      self.slavesInfo = []
      _item1 = None
      super().__init__(input)
      _slavesInfoLen = input.readUnsignedShort()
      for _i1 in range(0,_slavesInfoLen):
         _item1 = GameFightResumeSlaveInfo(input)
         self.slavesInfo.append(_item1)

   def resume(self):
      super().resume()
      for e in self.slavesInfo:
         e.resume()
