class GuildInfosUpgradeMessage:
   def __init__(self,input):
      self.spellId = []
      self.spellLevel = []
      _val9 = 0
      _val10 = 0
      self._maxTaxCollectorsCountFunc(input)
      self._taxCollectorsCountFunc(input)
      self._taxCollectorLifePointsFunc(input)
      self._taxCollectorDamagesBonusesFunc(input)
      self._taxCollectorPodsFunc(input)
      self._taxCollectorProspectingFunc(input)
      self._taxCollectorWisdomFunc(input)
      self._boostPointsFunc(input)
      _spellIdLen = input.readUnsignedShort()
      for _i9 in range(0,_spellIdLen):
         _val9 = input.readVarUhShort()
         if(_val9 < 0) :
            raise RuntimeError("Forbidden value (" + _val9 + ") on elements of spellId.")
         self.spellId.append(_val9)
      _spellLevelLen = input.readUnsignedShort()
      for _i10 in range(0,_spellLevelLen):
         _val10 = input.readShort()
         self.spellLevel.append(_val10)
   
   def _maxTaxCollectorsCountFunc(self,input) :
      self.maxTaxCollectorsCount = input.readByte()
      if(self.maxTaxCollectorsCount < 0) :
         raise RuntimeError("Forbidden value (" + self.maxTaxCollectorsCount + ") on element of GuildInfosUpgradeMessage.maxTaxCollectorsCount.")
   
   def _taxCollectorsCountFunc(self,input) :
      self.taxCollectorsCount = input.readByte()
      if(self.taxCollectorsCount < 0) :
         raise RuntimeError("Forbidden value (" + self.taxCollectorsCount + ") on element of GuildInfosUpgradeMessage.taxCollectorsCount.")
   
   def _taxCollectorLifePointsFunc(self,input) :
      self.taxCollectorLifePoints = input.readVarUhShort()
      if(self.taxCollectorLifePoints < 0) :
         raise RuntimeError("Forbidden value (" + self.taxCollectorLifePoints + ") on element of GuildInfosUpgradeMessage.taxCollectorLifePoints.")
   
   def _taxCollectorDamagesBonusesFunc(self,input) :
      self.taxCollectorDamagesBonuses = input.readVarUhShort()
      if(self.taxCollectorDamagesBonuses < 0) :
         raise RuntimeError("Forbidden value (" + self.taxCollectorDamagesBonuses + ") on element of GuildInfosUpgradeMessage.taxCollectorDamagesBonuses.")
   
   def _taxCollectorPodsFunc(self,input) :
      self.taxCollectorPods = input.readVarUhShort()
      if(self.taxCollectorPods < 0) :
         raise RuntimeError("Forbidden value (" + self.taxCollectorPods + ") on element of GuildInfosUpgradeMessage.taxCollectorPods.")
   
   def _taxCollectorProspectingFunc(self,input) :
      self.taxCollectorProspecting = input.readVarUhShort()
      if(self.taxCollectorProspecting < 0) :
         raise RuntimeError("Forbidden value (" + self.taxCollectorProspecting + ") on element of GuildInfosUpgradeMessage.taxCollectorProspecting.")
   
   def _taxCollectorWisdomFunc(self,input) :
      self.taxCollectorWisdom = input.readVarUhShort()
      if(self.taxCollectorWisdom < 0) :
         raise RuntimeError("Forbidden value (" + self.taxCollectorWisdom + ") on element of GuildInfosUpgradeMessage.taxCollectorWisdom.")
   
   def _boostPointsFunc(self,input) :
      self.boostPoints = input.readVarUhShort()
      if(self.boostPoints < 0) :
         raise RuntimeError("Forbidden value (" + self.boostPoints + ") on element of GuildInfosUpgradeMessage.boostPoints.")