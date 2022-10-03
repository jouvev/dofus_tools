from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._reasonFunc(input)
      self._memberIdFunc(input)
      self._memberAccountIdFunc(input)
      self._memberNameFunc(input)
      self._fightIdFunc(input)
      self._timeBeforeFightStartFunc(input)
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()
      if(self.reason < 0) :
         raise RuntimeError("Forbidden value (" + self.reason + ") on element of AbstractPartyMemberInFightMessage.reason.")
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.memberId + ") on element of AbstractPartyMemberInFightMessage.memberId.")
   
   def _memberAccountIdFunc(self,input) :
      self.memberAccountId = input.readInt()
      if(self.memberAccountId < 0) :
         raise RuntimeError("Forbidden value (" + self.memberAccountId + ") on element of AbstractPartyMemberInFightMessage.memberAccountId.")
   
   def _memberNameFunc(self,input) :
      self.memberName = input.readUTF()
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + self.fightId + ") on element of AbstractPartyMemberInFightMessage.fightId.")
   
   def _timeBeforeFightStartFunc(self,input) :
      self.timeBeforeFightStart = input.readVarShort()