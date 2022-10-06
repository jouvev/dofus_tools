class AccountCapabilitiesMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._accountIdFunc(input)
      self._breedsVisibleFunc(input)
      self._breedsAvailableFunc(input)
      self._statusFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.tutorialAvailable = bool(bin(_box0)[2:].zfill(8)[0])
      self.canCreateNewCharacter = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of AccountCapabilitiesMessage.accountId.")
   
   def _breedsVisibleFunc(self,input) :
      self.breedsVisible = input.readVarUhInt()
      if(self.breedsVisible < 0) :
         raise RuntimeError("Forbidden value (" + str(self.breedsVisible) + ") on element of AccountCapabilitiesMessage.breedsVisible.")
   
   def _breedsAvailableFunc(self,input) :
      self.breedsAvailable = input.readVarUhInt()
      if(self.breedsAvailable < 0) :
         raise RuntimeError("Forbidden value (" + str(self.breedsAvailable) + ") on element of AccountCapabilitiesMessage.breedsAvailable.")
   
   def _statusFunc(self,input) :
      self.status = input.readByte()

   def resume(self):
      print("accountId :",self.accountId)
      print("breedsVisible :",self.breedsVisible)
      print("breedsAvailable :",self.breedsAvailable)
      print("status :",self.status)
