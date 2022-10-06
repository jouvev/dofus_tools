from src.reseau.types.ObjectEffectInteger import ObjectEffectInteger

class MountClientData:
   def __init__(self,input):
      self.ancestor = []
      self.behaviors = []
      self.effectList = []
      _val3 = 0
      _val4 = 0
      _item34 = None
      self.deserializeByteBoxes(input)
      self._idFunc(input)
      self._modelFunc(input)
      _ancestorLen = input.readUnsignedShort()
      for _i3 in range(0,_ancestorLen):
         _val3 = input.readInt()
         if(_val3 < 0) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of ancestor.")
         self.ancestor.append(_val3)
      _behaviorsLen = input.readUnsignedShort()
      for _i4 in range(0,_behaviorsLen):
         _val4 = input.readInt()
         if(_val4 < 0) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of behaviors.")
         self.behaviors.append(_val4)
      self._nameFunc(input)
      self._ownerIdFunc(input)
      self._experienceFunc(input)
      self._experienceForLevelFunc(input)
      self._experienceForNextLevelFunc(input)
      self._levelFunc(input)
      self._maxPodsFunc(input)
      self._staminaFunc(input)
      self._staminaMaxFunc(input)
      self._maturityFunc(input)
      self._maturityForAdultFunc(input)
      self._energyFunc(input)
      self._energyMaxFunc(input)
      self._serenityFunc(input)
      self._aggressivityMaxFunc(input)
      self._serenityMaxFunc(input)
      self._loveFunc(input)
      self._loveMaxFunc(input)
      self._fecondationTimeFunc(input)
      self._boostLimiterFunc(input)
      self._boostMaxFunc(input)
      self._reproductionCountFunc(input)
      self._reproductionCountMaxFunc(input)
      self._harnessGIDFunc(input)
      _effectListLen = input.readUnsignedShort()
      for _i34 in range(0,_effectListLen):
         _item34 = ObjectEffectInteger(input)
         self.effectList.append(_item34)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.sex = bool(bin(_box0)[2:].zfill(8)[0])
      self.isRideable = bool(bin(_box0)[2:].zfill(8)[1])
      self.isWild = bool(bin(_box0)[2:].zfill(8)[2])
      self.isFecondationReady = bool(bin(_box0)[2:].zfill(8)[3])
      self.useHarnessColors = bool(bin(_box0)[2:].zfill(8)[4])
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < -9007199254740992 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of MountClientData.id.")
   
   def _modelFunc(self,input) :
      self.model = input.readVarUhInt()
      if(self.model < 0) :
         raise RuntimeError("Forbidden value (" + str(self.model) + ") on element of MountClientData.model.")
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _ownerIdFunc(self,input) :
      self.ownerId = input.readInt()
      if(self.ownerId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.ownerId) + ") on element of MountClientData.ownerId.")
   
   def _experienceFunc(self,input) :
      self.experience = input.readVarUhLong()
      if(self.experience < 0 or self.experience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of MountClientData.experience.")
   
   def _experienceForLevelFunc(self,input) :
      self.experienceForLevel = input.readVarUhLong()
      if(self.experienceForLevel < 0 or self.experienceForLevel > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experienceForLevel) + ") on element of MountClientData.experienceForLevel.")
   
   def _experienceForNextLevelFunc(self,input) :
      self.experienceForNextLevel = input.readDouble()
      if(self.experienceForNextLevel < -9007199254740992 or self.experienceForNextLevel > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experienceForNextLevel) + ") on element of MountClientData.experienceForNextLevel.")
   
   def _levelFunc(self,input) :
      self.level = input.readByte()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of MountClientData.level.")
   
   def _maxPodsFunc(self,input) :
      self.maxPods = input.readVarUhInt()
      if(self.maxPods < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxPods) + ") on element of MountClientData.maxPods.")
   
   def _staminaFunc(self,input) :
      self.stamina = input.readVarUhInt()
      if(self.stamina < 0) :
         raise RuntimeError("Forbidden value (" + str(self.stamina) + ") on element of MountClientData.stamina.")
   
   def _staminaMaxFunc(self,input) :
      self.staminaMax = input.readVarUhInt()
      if(self.staminaMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.staminaMax) + ") on element of MountClientData.staminaMax.")
   
   def _maturityFunc(self,input) :
      self.maturity = input.readVarUhInt()
      if(self.maturity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maturity) + ") on element of MountClientData.maturity.")
   
   def _maturityForAdultFunc(self,input) :
      self.maturityForAdult = input.readVarUhInt()
      if(self.maturityForAdult < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maturityForAdult) + ") on element of MountClientData.maturityForAdult.")
   
   def _energyFunc(self,input) :
      self.energy = input.readVarUhInt()
      if(self.energy < 0) :
         raise RuntimeError("Forbidden value (" + str(self.energy) + ") on element of MountClientData.energy.")
   
   def _energyMaxFunc(self,input) :
      self.energyMax = input.readVarUhInt()
      if(self.energyMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.energyMax) + ") on element of MountClientData.energyMax.")
   
   def _serenityFunc(self,input) :
      self.serenity = input.readInt()
   
   def _aggressivityMaxFunc(self,input) :
      self.aggressivityMax = input.readInt()
   
   def _serenityMaxFunc(self,input) :
      self.serenityMax = input.readVarUhInt()
      if(self.serenityMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.serenityMax) + ") on element of MountClientData.serenityMax.")
   
   def _loveFunc(self,input) :
      self.love = input.readVarUhInt()
      if(self.love < 0) :
         raise RuntimeError("Forbidden value (" + str(self.love) + ") on element of MountClientData.love.")
   
   def _loveMaxFunc(self,input) :
      self.loveMax = input.readVarUhInt()
      if(self.loveMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.loveMax) + ") on element of MountClientData.loveMax.")
   
   def _fecondationTimeFunc(self,input) :
      self.fecondationTime = input.readInt()
   
   def _boostLimiterFunc(self,input) :
      self.boostLimiter = input.readInt()
      if(self.boostLimiter < 0) :
         raise RuntimeError("Forbidden value (" + str(self.boostLimiter) + ") on element of MountClientData.boostLimiter.")
   
   def _boostMaxFunc(self,input) :
      self.boostMax = input.readDouble()
      if(self.boostMax < -9007199254740992 or self.boostMax > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.boostMax) + ") on element of MountClientData.boostMax.")
   
   def _reproductionCountFunc(self,input) :
      self.reproductionCount = input.readInt()
   
   def _reproductionCountMaxFunc(self,input) :
      self.reproductionCountMax = input.readVarUhInt()
      if(self.reproductionCountMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.reproductionCountMax) + ") on element of MountClientData.reproductionCountMax.")
   
   def _harnessGIDFunc(self,input) :
      self.harnessGID = input.readVarUhInt()
      if(self.harnessGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.harnessGID) + ") on element of MountClientData.harnessGID.")

   def resume(self):
      print("id :",self.id)
      print("model :",self.model)
      print("name :",self.name)
      print("ownerId :",self.ownerId)
      print("experience :",self.experience)
      print("experienceForLevel :",self.experienceForLevel)
      print("experienceForNextLevel :",self.experienceForNextLevel)
      print("level :",self.level)
      print("maxPods :",self.maxPods)
      print("stamina :",self.stamina)
      print("staminaMax :",self.staminaMax)
      print("maturity :",self.maturity)
      print("maturityForAdult :",self.maturityForAdult)
      print("energy :",self.energy)
      print("energyMax :",self.energyMax)
      print("serenity :",self.serenity)
      print("aggressivityMax :",self.aggressivityMax)
      print("serenityMax :",self.serenityMax)
      print("love :",self.love)
      print("loveMax :",self.loveMax)
      print("fecondationTime :",self.fecondationTime)
      print("boostLimiter :",self.boostLimiter)
      print("boostMax :",self.boostMax)
      print("reproductionCount :",self.reproductionCount)
      print("reproductionCountMax :",self.reproductionCountMax)
      print("harnessGID :",self.harnessGID)
      print("ancestor :",self.ancestor)
      print("behaviors :",self.behaviors)
      for e in self.effectList:
         e.resume()
