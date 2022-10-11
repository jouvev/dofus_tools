import src.reseau.TypesFactory as pf
from src.reseau.types.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo

class PrismFightersInformation:
   def __init__(self,input):
      self.allyCharactersInformations = []
      self.enemyCharactersInformations = []
      _id3 = 0
      _item3 = None
      _id4 = 0
      _item4 = None
      self._subAreaIdFunc(input)
      self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo(input)
      _allyCharactersInformationsLen = input.readUnsignedShort()
      for _i3 in range(0,_allyCharactersInformationsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.allyCharactersInformations.append(_item3)
      _enemyCharactersInformationsLen = input.readUnsignedShort()
      for _i4 in range(0,_enemyCharactersInformationsLen):
         _id4 = input.readUnsignedShort()
         _item4 = pf.TypesFactory.get_instance_id(_id4,input)
         self.enemyCharactersInformations.append(_item4)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismFightersInformation.subAreaId.")

   def resume(self):
      print("subAreaId :",self.subAreaId)
      self.waitingForHelpInfo.resume()
      for e in self.allyCharactersInformations:
         e.resume()
      for e in self.enemyCharactersInformations:
         e.resume()
