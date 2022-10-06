from src.reseau.messages.GameActionFightDispellMessage import GameActionFightDispellMessage

class GameActionFightDispellSpellMessage(GameActionFightDispellMessage):
   def __init__(self,input):
      super().__init__(input)
      self._spellIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of GameActionFightDispellSpellMessage.spellId.")

   def resume(self):
      super().resume()
      print("spellId :",self.spellId)
