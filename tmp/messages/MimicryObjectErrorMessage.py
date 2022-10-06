from tmp.messages.SymbioticObjectErrorMessage import SymbioticObjectErrorMessage

class MimicryObjectErrorMessage(SymbioticObjectErrorMessage):
   def __init__(self,input):
      super().__init__(input)
      self._previewFunc(input)
   
   def _previewFunc(self,input) :
      self.preview = input.readBoolean()

   def resume(self):
      super().resume()
      print("preview :",self.preview)
