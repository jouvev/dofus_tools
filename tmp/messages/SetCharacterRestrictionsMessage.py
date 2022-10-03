from tmp.types.ActorRestrictionsInformations import ActorRestrictionsInformations
class SetCharacterRestrictionsMessage:
   def __init__(self,input):
      self._actorIdFunc(input)
      self.restrictions = ActorRestrictionsInformations(input)
   
   def _actorIdFunc(self,input) :
      self.actorId = input.readDouble()
      if(self.actorId < -9007199254740992 or self.actorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.actorId + ") on element of SetCharacterRestrictionsMessage.actorId.")