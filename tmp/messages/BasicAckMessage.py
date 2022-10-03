class BasicAckMessage:
   def __init__(self,input):
      self._seqFunc(input)
      self._lastPacketIdFunc(input)
   
   def _seqFunc(self,input) :
      self.seq = input.readVarUhInt()
      if(self.seq < 0) :
         raise RuntimeError("Forbidden value (" + self.seq + ") on element of BasicAckMessage.seq.")
   
   def _lastPacketIdFunc(self,input) :
      self.lastPacketId = input.readVarUhShort()
      if(self.lastPacketId < 0) :
         raise RuntimeError("Forbidden value (" + self.lastPacketId + ") on element of BasicAckMessage.lastPacketId.")