from tmp.messages.AbstractGameActionFightTargetedAbilityMessage import AbstractGameActionFightTargetedAbilityMessage
class GameActionFightCloseCombatMessage(AbstractGameActionFightTargetedAbilityMessage):
   def __init__(self,input):
      super().__init__(input)
      self._weaponGenericIdFunc(input)
   
   def _weaponGenericIdFunc(self,input) :
      self.weaponGenericId = input.readVarUhInt()
      if(self.weaponGenericId < 0) :
         raise RuntimeError("Forbidden value (" + self.weaponGenericId + ") on element of GameActionFightCloseCombatMessage.weaponGenericId.")