class MoodSmileyResultMessage:
   def __init__(self,input):
      self._resultCodeFunc(input)
      self._smileyIdFunc(input)
   
   def _resultCodeFunc(self,input) :
      self.resultCode = input.readByte()
      if(self.resultCode < 0) :
         raise RuntimeError("Forbidden value (" + self.resultCode + ") on element of MoodSmileyResultMessage.resultCode.")
   
   def _smileyIdFunc(self,input) :
      self.smileyId = input.readVarUhShort()
      if(self.smileyId < 0) :
         raise RuntimeError("Forbidden value (" + self.smileyId + ") on element of MoodSmileyResultMessage.smileyId.")