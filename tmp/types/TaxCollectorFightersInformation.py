import tmp.TypesFactory as pf
class TaxCollectorFightersInformation:
   def __init__(self,input):
      self.allyCharactersInformations = []
      self.enemyCharactersInformations = []
      _id2 = 0
      _item2 = None
      _id3 = 0
      _item3 = None
      self._collectorIdFunc(input)
      _allyCharactersInformationsLen = input.readUnsignedShort()
      for _i2 in range(0,_allyCharactersInformationsLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.allyCharactersInformations.append(_item2)
      _enemyCharactersInformationsLen = input.readUnsignedShort()
      for _i3 in range(0,_enemyCharactersInformationsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.enemyCharactersInformations.append(_item3)
   
   def _collectorIdFunc(self,input) :
      self.collectorId = input.readDouble()
      if(self.collectorId < 0 or self.collectorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.collectorId + ") on element of TaxCollectorFightersInformation.collectorId.")