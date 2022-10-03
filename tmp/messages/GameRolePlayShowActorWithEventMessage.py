from tmp.messages.GameRolePlayShowActorMessage import GameRolePlayShowActorMessage
class GameRolePlayShowActorWithEventMessage(GameRolePlayShowActorMessage):
   def __init__(self,input):
      super().__init__(input)
      self._actorEventIdFunc(input)
   
   def _actorEventIdFunc(self,input) :
      self.actorEventId = input.readByte()
      if(self.actorEventId < 0) :
         raise RuntimeError("Forbidden value (" + self.actorEventId + ") on element of GameRolePlayShowActorWithEventMessage.actorEventId.")