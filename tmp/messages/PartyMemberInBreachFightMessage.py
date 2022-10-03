from tmp.messages.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
   def __init__(self,input):
      super().__init__(input)
      self._floorFunc(input)
      self._roomFunc(input)
   
   def _floorFunc(self,input) :
      self.floor = input.readVarUhInt()
      if(self.floor < 0) :
         raise RuntimeError("Forbidden value (" + self.floor + ") on element of PartyMemberInBreachFightMessage.floor.")
   
   def _roomFunc(self,input) :
      self.room = input.readByte()
      if(self.room < 0) :
         raise RuntimeError("Forbidden value (" + self.room + ") on element of PartyMemberInBreachFightMessage.room.")