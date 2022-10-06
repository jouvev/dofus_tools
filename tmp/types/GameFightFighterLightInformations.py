class GameFightFighterLightInformations:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._idFunc(input)
      self._waveFunc(input)
      self._levelFunc(input)
      self._breedFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.sex = bool(bin(_box0)[2:].zfill(8)[0])
      self.alive = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < -9007199254740992 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of GameFightFighterLightInformations.id.")
   
   def _waveFunc(self,input) :
      self.wave = input.readByte()
      if(self.wave < 0) :
         raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element of GameFightFighterLightInformations.wave.")
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameFightFighterLightInformations.level.")
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()

   def resume(self):
      print("id :",self.id)
      print("wave :",self.wave)
      print("level :",self.level)
      print("breed :",self.breed)
