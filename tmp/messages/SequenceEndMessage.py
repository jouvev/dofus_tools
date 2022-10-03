class SequenceEndMessage:
   def __init__(self,input):
      self._actionIdFunc(input)
      self._authorIdFunc(input)
      self._sequenceTypeFunc(input)
   
   def _actionIdFunc(self,input) :
      self.actionId = input.readVarUhShort()
      if(self.actionId < 0) :
         raise RuntimeError("Forbidden value (" + self.actionId + ") on element of SequenceEndMessage.actionId.")
   
   def _authorIdFunc(self,input) :
      self.authorId = input.readDouble()
      if(self.authorId < -9007199254740992 or self.authorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.authorId + ") on element of SequenceEndMessage.authorId.")
   
   def _sequenceTypeFunc(self,input) :
      self.sequenceType = input.readByte()