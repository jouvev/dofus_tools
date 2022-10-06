from tmp.types.ObjectItem import ObjectItem
from tmp.types.PrismInformation import PrismInformation

class AllianceInsiderPrismInformation(PrismInformation):
   def __init__(self,input):
      self.modulesObjects = []
      _item5 = None
      super().__init__(input)
      self._lastTimeSlotModificationDateFunc(input)
      self._lastTimeSlotModificationAuthorGuildIdFunc(input)
      self._lastTimeSlotModificationAuthorIdFunc(input)
      self._lastTimeSlotModificationAuthorNameFunc(input)
      _modulesObjectsLen = input.readUnsignedShort()
      for _i5 in range(0,_modulesObjectsLen):
         _item5 = ObjectItem(input)
         self.modulesObjects.append(_item5)
   
   def _lastTimeSlotModificationDateFunc(self,input) :
      self.lastTimeSlotModificationDate = input.readInt()
      if(self.lastTimeSlotModificationDate < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationDate) + ") on element of AllianceInsiderPrismInformation.lastTimeSlotModificationDate.")
   
   def _lastTimeSlotModificationAuthorGuildIdFunc(self,input) :
      self.lastTimeSlotModificationAuthorGuildId = input.readVarUhInt()
      if(self.lastTimeSlotModificationAuthorGuildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationAuthorGuildId) + ") on element of AllianceInsiderPrismInformation.lastTimeSlotModificationAuthorGuildId.")
   
   def _lastTimeSlotModificationAuthorIdFunc(self,input) :
      self.lastTimeSlotModificationAuthorId = input.readVarUhLong()
      if(self.lastTimeSlotModificationAuthorId < 0 or self.lastTimeSlotModificationAuthorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationAuthorId) + ") on element of AllianceInsiderPrismInformation.lastTimeSlotModificationAuthorId.")
   
   def _lastTimeSlotModificationAuthorNameFunc(self,input) :
      self.lastTimeSlotModificationAuthorName = input.readUTF()

   def resume(self):
      super().resume()
      print("lastTimeSlotModificationDate :",self.lastTimeSlotModificationDate)
      print("lastTimeSlotModificationAuthorGuildId :",self.lastTimeSlotModificationAuthorGuildId)
      print("lastTimeSlotModificationAuthorId :",self.lastTimeSlotModificationAuthorId)
      print("lastTimeSlotModificationAuthorName :",self.lastTimeSlotModificationAuthorName)
      for e in self.modulesObjects:
         e.resume()
