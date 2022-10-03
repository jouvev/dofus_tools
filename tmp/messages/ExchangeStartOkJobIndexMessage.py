class ExchangeStartOkJobIndexMessage:
   def __init__(self,input):
      self.jobs = []
      _val1 = 0
      _jobsLen = input.readUnsignedShort()
      for _i1 in range(0,_jobsLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of jobs.")
         self.jobs.append(_val1)