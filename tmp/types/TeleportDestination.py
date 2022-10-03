class TeleportDestination:
   def __init__(self,input):
      self._typeFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      self._levelFunc(input)
      self._costFunc(input)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + self.type + ") on element of TeleportDestination.type.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of TeleportDestination.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of TeleportDestination.subAreaId.")
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of TeleportDestination.level.")
   
   def _costFunc(self,input) :
      self.cost = input.readVarUhShort()
      if(self.cost < 0) :
         raise RuntimeError("Forbidden value (" + self.cost + ") on element of TeleportDestination.cost.")