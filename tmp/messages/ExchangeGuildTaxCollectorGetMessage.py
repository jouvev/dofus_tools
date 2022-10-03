from tmp.types.ObjectItemGenericQuantity import ObjectItemGenericQuantity
class ExchangeGuildTaxCollectorGetMessage:
   def __init__(self,input):
      self.objectsInfos = []
      _item11 = None
      self._collectorNameFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      self._userNameFunc(input)
      self._callerIdFunc(input)
      self._callerNameFunc(input)
      self._experienceFunc(input)
      self._podsFunc(input)
      _objectsInfosLen = input.readUnsignedShort()
      for _i11 in range(0,_objectsInfosLen):
         _item11 = ObjectItemGenericQuantity(input)
         self.objectsInfos.append(_item11)
   
   def _collectorNameFunc(self,input) :
      self.collectorName = input.readUTF()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + self.worldX + ") on element of ExchangeGuildTaxCollectorGetMessage.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + self.worldY + ") on element of ExchangeGuildTaxCollectorGetMessage.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of ExchangeGuildTaxCollectorGetMessage.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of ExchangeGuildTaxCollectorGetMessage.subAreaId.")
   
   def _userNameFunc(self,input) :
      self.userName = input.readUTF()
   
   def _callerIdFunc(self,input) :
      self.callerId = input.readVarUhLong()
      if(self.callerId < 0 or self.callerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.callerId + ") on element of ExchangeGuildTaxCollectorGetMessage.callerId.")
   
   def _callerNameFunc(self,input) :
      self.callerName = input.readUTF()
   
   def _experienceFunc(self,input) :
      self.experience = input.readDouble()
      if(self.experience < -9007199254740992 or self.experience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experience + ") on element of ExchangeGuildTaxCollectorGetMessage.experience.")
   
   def _podsFunc(self,input) :
      self.pods = input.readVarUhShort()
      if(self.pods < 0) :
         raise RuntimeError("Forbidden value (" + self.pods + ") on element of ExchangeGuildTaxCollectorGetMessage.pods.")