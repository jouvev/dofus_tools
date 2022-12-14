from src.reseau.types.CharacterSpellModification import CharacterSpellModification

class UpdateSpellModifierMessage:
   def __init__(self,input):
      self._actorIdFunc(input)
      self.spellModifier = CharacterSpellModification(input)
   
   def _actorIdFunc(self,input) :
      self.actorId = input.readDouble()
      if(self.actorId < -9007199254740992 or self.actorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.actorId) + ") on element of UpdateSpellModifierMessage.actorId.")

   def resume(self):
      print("actorId :",self.actorId)
      self.spellModifier.resume()
