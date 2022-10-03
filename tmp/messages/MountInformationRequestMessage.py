class MountInformationRequestMessage:
   def __init__(self,input):
      self._idFunc(input)
      self._timeFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < -9007199254740992 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of MountInformationRequestMessage.id.")
   
   def _timeFunc(self,input) :
      self.time = input.readDouble()
      if(self.time < -9007199254740992 or self.time > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.time + ") on element of MountInformationRequestMessage.time.")