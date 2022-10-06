import tmp.TypesFactory as pf

class AlterationInfo:
   def __init__(self,input):
      self.effects = []
      _id5 = 0
      _item5 = None
      self._alterationIdFunc(input)
      self._creationTimeFunc(input)
      self._expirationTypeFunc(input)
      self._expirationValueFunc(input)
      _effectsLen = input.readUnsignedShort()
      for _i5 in range(0,_effectsLen):
         _id5 = input.readUnsignedShort()
         _item5 = pf.TypesFactory.get_instance_id(_id5,input)
         self.effects.append(_item5)
   
   def _alterationIdFunc(self,input) :
      self.alterationId = input.readUnsignedInt()
      if(self.alterationId < 0 or self.alterationId > 4294967295) :
         raise RuntimeError("Forbidden value (" + str(self.alterationId) + ") on element of AlterationInfo.alterationId.")
   
   def _creationTimeFunc(self,input) :
      self.creationTime = input.readDouble()
      if(self.creationTime < -9007199254740992 or self.creationTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.creationTime) + ") on element of AlterationInfo.creationTime.")
   
   def _expirationTypeFunc(self,input) :
      self.expirationType = input.readByte()
      if(self.expirationType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.expirationType) + ") on element of AlterationInfo.expirationType.")
   
   def _expirationValueFunc(self,input) :
      self.expirationValue = input.readDouble()
      if(self.expirationValue < -9007199254740992 or self.expirationValue > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.expirationValue) + ") on element of AlterationInfo.expirationValue.")

   def resume(self):
      print("alterationId :",self.alterationId)
      print("creationTime :",self.creationTime)
      print("expirationType :",self.expirationType)
      print("expirationValue :",self.expirationValue)
      for e in self.effects:
         e.resume()
