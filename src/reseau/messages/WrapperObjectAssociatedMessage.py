from src.reseau.messages.SymbioticObjectAssociatedMessage import SymbioticObjectAssociatedMessage

class WrapperObjectAssociatedMessage(SymbioticObjectAssociatedMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
