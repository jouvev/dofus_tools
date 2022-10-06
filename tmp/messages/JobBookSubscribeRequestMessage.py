class JobBookSubscribeRequestMessage:
   def __init__(self,input):
      self.jobIds = []
      _val1 = 0
      _jobIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_jobIdsLen):
         _val1 = input.readByte()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of jobIds.")
         self.jobIds.append(_val1)

   def resume(self):
      print("jobIds :",self.jobIds)
