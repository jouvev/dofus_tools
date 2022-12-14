from src.reseau.messages.EmotePlayAbstractMessage import EmotePlayAbstractMessage

class EmotePlayMassiveMessage(EmotePlayAbstractMessage):
   def __init__(self,input):
      self.actorIds = []
      _val1 = None
      super().__init__(input)
      _actorIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_actorIdsLen):
         _val1 = input.readDouble()
         if(_val1 < -9007199254740992 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of actorIds.")
         self.actorIds.append(_val1)

   def resume(self):
      super().resume()
      print("actorIds :",self.actorIds)
