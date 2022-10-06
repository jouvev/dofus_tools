class GameServerInformations:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._idFunc(input)
      self._typeFunc(input)
      self._statusFunc(input)
      self._completionFunc(input)
      self._charactersCountFunc(input)
      self._charactersSlotsFunc(input)
      self._dateFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.isMonoAccount = bool(bin(_box0)[2:].zfill(8)[0])
      self.isSelectable = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _idFunc(self,input) :
      self.id = input.readVarUhShort()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of GameServerInformations.id.")
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
   
   def _statusFunc(self,input) :
      self.status = input.readByte()
      if(self.status < 0) :
         raise RuntimeError("Forbidden value (" + str(self.status) + ") on element of GameServerInformations.status.")
   
   def _completionFunc(self,input) :
      self.completion = input.readByte()
      if(self.completion < 0) :
         raise RuntimeError("Forbidden value (" + str(self.completion) + ") on element of GameServerInformations.completion.")
   
   def _charactersCountFunc(self,input) :
      self.charactersCount = input.readByte()
      if(self.charactersCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.charactersCount) + ") on element of GameServerInformations.charactersCount.")
   
   def _charactersSlotsFunc(self,input) :
      self.charactersSlots = input.readByte()
      if(self.charactersSlots < 0) :
         raise RuntimeError("Forbidden value (" + str(self.charactersSlots) + ") on element of GameServerInformations.charactersSlots.")
   
   def _dateFunc(self,input) :
      self.date = input.readDouble()
      if(self.date < -9007199254740992 or self.date > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.date) + ") on element of GameServerInformations.date.")

   def resume(self):
      print("id :",self.id)
      print("type :",self.type)
      print("status :",self.status)
      print("completion :",self.completion)
      print("charactersCount :",self.charactersCount)
      print("charactersSlots :",self.charactersSlots)
      print("date :",self.date)
