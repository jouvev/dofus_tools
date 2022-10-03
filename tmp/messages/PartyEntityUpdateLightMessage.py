from tmp.messages.PartyUpdateLightMessage import PartyUpdateLightMessage
class PartyEntityUpdateLightMessage(PartyUpdateLightMessage):
   def __init__(self,input):
      super().__init__(input)
      self._indexIdFunc(input)
   
   def _indexIdFunc(self,input) :
      self.indexId = input.readByte()
      if(self.indexId < 0) :
         raise RuntimeError("Forbidden value (" + self.indexId + ") on element of PartyEntityUpdateLightMessage.indexId.")