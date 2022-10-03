import tmp.TypesFactory as pf
from tmp.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
class MapComplementaryInformationsBreachMessage(MapComplementaryInformationsDataMessage):
   def __init__(self,input):
      self.branches = []
      _id4 = 0
      _item4 = None
      super().__init__(input)
      self._floorFunc(input)
      self._roomFunc(input)
      self._infinityModeFunc(input)
      _branchesLen = input.readUnsignedShort()
      for _i4 in range(0,_branchesLen):
         _id4 = input.readUnsignedShort()
         _item4 = pf.TypesFactory.get_instance_id(_id4,input)
         self.branches.append(_item4)
   
   def _floorFunc(self,input) :
      self.floor = input.readVarUhInt()
      if(self.floor < 0) :
         raise RuntimeError("Forbidden value (" + self.floor + ") on element of MapComplementaryInformationsBreachMessage.floor.")
   
   def _roomFunc(self,input) :
      self.room = input.readByte()
      if(self.room < 0) :
         raise RuntimeError("Forbidden value (" + self.room + ") on element of MapComplementaryInformationsBreachMessage.room.")
   
   def _infinityModeFunc(self,input) :
      self.infinityMode = input.readShort()
      if(self.infinityMode < 0) :
         raise RuntimeError("Forbidden value (" + self.infinityMode + ") on element of MapComplementaryInformationsBreachMessage.infinityMode.")