from tmp.messages.SymbioticObjectErrorMessage import SymbioticObjectErrorMessage
class WrapperObjectErrorMessage(SymbioticObjectErrorMessage):
   def __init__(self,input):
      super().__init__(input)