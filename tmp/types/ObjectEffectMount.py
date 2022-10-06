from tmp.types.ObjectEffectInteger import ObjectEffectInteger
from tmp.types.ObjectEffect import ObjectEffect

class ObjectEffectMount(ObjectEffect):
   def __init__(self,input):
      self.effects = []
      self.capacities = []
      _item13 = None
      _val14 = 0
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._idFunc(input)
      self._expirationDateFunc(input)
      self._modelFunc(input)
      self._nameFunc(input)
      self._ownerFunc(input)
      self._levelFunc(input)
      self._reproductionCountFunc(input)
      self._reproductionCountMaxFunc(input)
      _effectsLen = input.readUnsignedShort()
      for _i13 in range(0,_effectsLen):
         _item13 = ObjectEffectInteger(input)
         self.effects.append(_item13)
      _capacitiesLen = input.readUnsignedShort()
      for _i14 in range(0,_capacitiesLen):
         _val14 = input.readVarUhInt()
         if(_val14 < 0) :
            raise RuntimeError("Forbidden value (" + _val14 + ") on elements of capacities.")
         self.capacities.append(_val14)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.sex = bool(bin(_box0)[2:].zfill(8)[0])
      self.isRideable = bool(bin(_box0)[2:].zfill(8)[1])
      self.isFeconded = bool(bin(_box0)[2:].zfill(8)[2])
      self.isFecondationReady = bool(bin(_box0)[2:].zfill(8)[3])
   
   def _idFunc(self,input) :
      self.id = input.readVarUhLong()
      if(self.id < 0 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of ObjectEffectMount.id.")
   
   def _expirationDateFunc(self,input) :
      self.expirationDate = input.readVarUhLong()
      if(self.expirationDate < 0 or self.expirationDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.expirationDate) + ") on element of ObjectEffectMount.expirationDate.")
   
   def _modelFunc(self,input) :
      self.model = input.readVarUhInt()
      if(self.model < 0) :
         raise RuntimeError("Forbidden value (" + str(self.model) + ") on element of ObjectEffectMount.model.")
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _ownerFunc(self,input) :
      self.owner = input.readUTF()
   
   def _levelFunc(self,input) :
      self.level = input.readByte()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of ObjectEffectMount.level.")
   
   def _reproductionCountFunc(self,input) :
      self.reproductionCount = input.readVarInt()
   
   def _reproductionCountMaxFunc(self,input) :
      self.reproductionCountMax = input.readVarUhInt()
      if(self.reproductionCountMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.reproductionCountMax) + ") on element of ObjectEffectMount.reproductionCountMax.")

   def resume(self):
      super().resume()
      print("id :",self.id)
      print("expirationDate :",self.expirationDate)
      print("model :",self.model)
      print("name :",self.name)
      print("owner :",self.owner)
      print("level :",self.level)
      print("reproductionCount :",self.reproductionCount)
      print("reproductionCountMax :",self.reproductionCountMax)
      for e in self.effects:
         e.resume()
      print("capacities :",self.capacities)
