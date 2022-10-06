from src.reseau.messages.NpcDialogCreationMessage import NpcDialogCreationMessage

class PortalDialogCreationMessage(NpcDialogCreationMessage):
   def __init__(self,input):
      super().__init__(input)
      self._typeFunc(input)
   
   def _typeFunc(self,input) :
      self.type = input.readInt()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of PortalDialogCreationMessage.type.")

   def resume(self):
      super().resume()
      print("type :",self.type)
