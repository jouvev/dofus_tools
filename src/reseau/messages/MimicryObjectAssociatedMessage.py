from src.reseau.messages.SymbioticObjectAssociatedMessage import SymbioticObjectAssociatedMessage

class MimicryObjectAssociatedMessage(SymbioticObjectAssociatedMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
