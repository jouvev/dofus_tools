from tmp.messages.InteractiveUseRequestMessage import InteractiveUseRequestMessage

class InteractiveUseWithParamRequestMessage(InteractiveUseRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._idFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readInt()

   def resume(self):
      super().resume()
      print("id :",self.id)
