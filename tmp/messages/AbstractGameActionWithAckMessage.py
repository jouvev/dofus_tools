from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class AbstractGameActionWithAckMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._waitAckIdFunc(input)
   
   def _waitAckIdFunc(self,input) :
      self.waitAckId = input.readShort()

   def resume(self):
      super().resume()
      print("waitAckId :",self.waitAckId)
