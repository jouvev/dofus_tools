class SequenceStartMessage:
   def __init__(self,input):
      self._sequenceTypeFunc(input)
      self._authorIdFunc(input)
   
   def _sequenceTypeFunc(self,input) :
      self.sequenceType = input.readByte()
   
   def _authorIdFunc(self,input) :
      self.authorId = input.readDouble()
      if(self.authorId < -9007199254740992 or self.authorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.authorId + ") on element of SequenceStartMessage.authorId.")