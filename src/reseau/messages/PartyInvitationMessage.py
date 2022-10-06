from src.reseau.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyInvitationMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._partyTypeFunc(input)
      self._partyNameFunc(input)
      self._maxParticipantsFunc(input)
      self._fromIdFunc(input)
      self._fromNameFunc(input)
      self._toIdFunc(input)
   
   def _partyTypeFunc(self,input) :
      self.partyType = input.readByte()
      if(self.partyType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.partyType) + ") on element of PartyInvitationMessage.partyType.")
   
   def _partyNameFunc(self,input) :
      self.partyName = input.readUTF()
   
   def _maxParticipantsFunc(self,input) :
      self.maxParticipants = input.readByte()
      if(self.maxParticipants < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxParticipants) + ") on element of PartyInvitationMessage.maxParticipants.")
   
   def _fromIdFunc(self,input) :
      self.fromId = input.readVarUhLong()
      if(self.fromId < 0 or self.fromId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.fromId) + ") on element of PartyInvitationMessage.fromId.")
   
   def _fromNameFunc(self,input) :
      self.fromName = input.readUTF()
   
   def _toIdFunc(self,input) :
      self.toId = input.readVarUhLong()
      if(self.toId < 0 or self.toId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.toId) + ") on element of PartyInvitationMessage.toId.")

   def resume(self):
      super().resume()
      print("partyType :",self.partyType)
      print("partyName :",self.partyName)
      print("maxParticipants :",self.maxParticipants)
      print("fromId :",self.fromId)
      print("fromName :",self.fromName)
      print("toId :",self.toId)
