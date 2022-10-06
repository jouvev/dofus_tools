class MoodSmileyRequestMessage:
   def __init__(self,input):
      self._smileyIdFunc(input)
   
   def _smileyIdFunc(self,input) :
      self.smileyId = input.readVarUhShort()
      if(self.smileyId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.smileyId) + ") on element of MoodSmileyRequestMessage.smileyId.")

   def resume(self):
      print("smileyId :",self.smileyId)
