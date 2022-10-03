class EntityInformation:
   def __init__(self,input):
      self._idFunc(input)
      self._experienceFunc(input)
      self._statusFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhShort()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of EntityInformation.id.")
   
   def _experienceFunc(self,input) :
      self.experience = input.readVarUhInt()
      if(self.experience < 0) :
         raise RuntimeError("Forbidden value (" + self.experience + ") on element of EntityInformation.experience.")
   
   def _statusFunc(self,input) :
      self.status = input.readBoolean()