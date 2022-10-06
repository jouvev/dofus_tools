from src.reseau.messages.GameRolePlayShowActorMessage import GameRolePlayShowActorMessage

class GameRolePlayShowActorWithEventMessage(GameRolePlayShowActorMessage):
   def __init__(self,input):
      super().__init__(input)
      self._actorEventIdFunc(input)
   
   def _actorEventIdFunc(self,input) :
      self.actorEventId = input.readByte()
      if(self.actorEventId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.actorEventId) + ") on element of GameRolePlayShowActorWithEventMessage.actorEventId.")

   def resume(self):
      super().resume()
      print("actorEventId :",self.actorEventId)
