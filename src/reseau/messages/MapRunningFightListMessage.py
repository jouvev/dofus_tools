from src.reseau.types.FightExternalInformations import FightExternalInformations

class MapRunningFightListMessage:
   def __init__(self,input):
      self.fights = []
      _item1 = None
      _fightsLen = input.readUnsignedShort()
      for _i1 in range(0,_fightsLen):
         _item1 = FightExternalInformations(input)
         self.fights.append(_item1)

   def resume(self):
      for e in self.fights:
         e.resume()
