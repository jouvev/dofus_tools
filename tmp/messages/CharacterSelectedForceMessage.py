class CharacterSelectedForceMessage:
   def __init__(self,input):
      self._idFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readInt()
      if(self.id < 1 or self.id > 2147483647) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of CharacterSelectedForceMessage.id.")