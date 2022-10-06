from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._markIdFunc(input)
      self._markImpactCellFunc(input)
      self._triggeringCharacterIdFunc(input)
      self._triggeredSpellIdFunc(input)
   
   def _markIdFunc(self,input) :
      self.markId = input.readShort()
   
   def _markImpactCellFunc(self,input) :
      self.markImpactCell = input.readVarUhShort()
      if(self.markImpactCell < 0) :
         raise RuntimeError("Forbidden value (" + str(self.markImpactCell) + ") on element of GameActionFightTriggerGlyphTrapMessage.markImpactCell.")
   
   def _triggeringCharacterIdFunc(self,input) :
      self.triggeringCharacterId = input.readDouble()
      if(self.triggeringCharacterId < -9007199254740992 or self.triggeringCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.triggeringCharacterId) + ") on element of GameActionFightTriggerGlyphTrapMessage.triggeringCharacterId.")
   
   def _triggeredSpellIdFunc(self,input) :
      self.triggeredSpellId = input.readVarUhShort()
      if(self.triggeredSpellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.triggeredSpellId) + ") on element of GameActionFightTriggerGlyphTrapMessage.triggeredSpellId.")

   def resume(self):
      super().resume()
      print("markId :",self.markId)
      print("markImpactCell :",self.markImpactCell)
      print("triggeringCharacterId :",self.triggeringCharacterId)
      print("triggeredSpellId :",self.triggeredSpellId)
