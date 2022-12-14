from src.reseau.messages.CurrentMapMessage import CurrentMapMessage

class CurrentMapInstanceMessage(CurrentMapMessage):
   def __init__(self,input):
      super().__init__(input)
      self._instantiatedMapIdFunc(input)
   
   def _instantiatedMapIdFunc(self,input) :
      self.instantiatedMapId = input.readDouble()
      if(self.instantiatedMapId < 0 or self.instantiatedMapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.instantiatedMapId) + ") on element of CurrentMapInstanceMessage.instantiatedMapId.")

   def resume(self):
      super().resume()
      print("instantiatedMapId :",self.instantiatedMapId)
