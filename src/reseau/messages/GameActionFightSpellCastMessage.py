from src.reseau.messages.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage

class GameActionFightSpellCastMessage(AbstractGameActionFightTargetedAbilityMessage):
   def __init__(self,input):
      self.portalsIds = []
      _val3 = 0
      super().__init__(input)
      self._spellIdFunc(input)
      self._spellLevelFunc(input)
      _portalsIdsLen = input.readUnsignedShort()
      for _i3 in range(0,_portalsIdsLen):
         _val3 = input.readShort()
         self.portalsIds.append(_val3)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of GameActionFightSpellCastMessage.spellId.")
   
   def _spellLevelFunc(self,input) :
      self.spellLevel = input.readShort()
      if(self.spellLevel < 1 or self.spellLevel > 32767) :
         raise RuntimeError("Forbidden value (" + str(self.spellLevel) + ") on element of GameActionFightSpellCastMessage.spellLevel.")

   def resume(self):
      super().resume()
      print("spellId :",self.spellId)
      print("spellLevel :",self.spellLevel)
      print("portalsIds :",self.portalsIds)
