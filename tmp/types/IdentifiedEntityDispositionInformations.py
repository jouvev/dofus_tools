from tmp.types.EntityDispositionInformations import EntityDispositionInformations
class IdentifiedEntityDispositionInformations(EntityDispositionInformations):
   def __init__(self,input):
      super().__init__(input)
      self._idFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < -9007199254740992 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of IdentifiedEntityDispositionInformations.id.")