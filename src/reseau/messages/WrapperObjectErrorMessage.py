from src.reseau.messages.SymbioticObjectErrorMessage import SymbioticObjectErrorMessage

class WrapperObjectErrorMessage(SymbioticObjectErrorMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
