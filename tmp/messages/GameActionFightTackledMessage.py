from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightTackledMessage(AbstractGameActionMessage):
   def __init__(self,input):
      self.tacklersIds = []
      _val1 = None
      super().__init__(input)
      _tacklersIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_tacklersIdsLen):
         _val1 = input.readDouble()
         if(_val1 < -9007199254740992 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of tacklersIds.")
         self.tacklersIds.append(_val1)

   def resume(self):
      super().resume()
      print("tacklersIds :",self.tacklersIds)
