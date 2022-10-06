from tmp.messages.GameActionFightDispellMessage import GameActionFightDispellMessage

class GameActionFightDispellEffectMessage(GameActionFightDispellMessage):
   def __init__(self,input):
      super().__init__(input)
      self._boostUIDFunc(input)
   
   def _boostUIDFunc(self,input) :
      self.boostUID = input.readInt()
      if(self.boostUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.boostUID) + ") on element of GameActionFightDispellEffectMessage.boostUID.")

   def resume(self):
      super().resume()
      print("boostUID :",self.boostUID)
