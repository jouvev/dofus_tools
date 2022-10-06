from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightActivateGlyphTrapMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._markIdFunc(input)
      self._activeFunc(input)
   
   def _markIdFunc(self,input) :
      self.markId = input.readShort()
   
   def _activeFunc(self,input) :
      self.active = input.readBoolean()

   def resume(self):
      super().resume()
      print("markId :",self.markId)
      print("active :",self.active)
