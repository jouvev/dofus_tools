from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightUnmarkCellsMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._markIdFunc(input)
   
   def _markIdFunc(self,input) :
      self.markId = input.readShort()

   def resume(self):
      super().resume()
      print("markId :",self.markId)
