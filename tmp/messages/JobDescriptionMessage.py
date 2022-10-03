from tmp.types.JobDescription import JobDescription
class JobDescriptionMessage:
   def __init__(self,input):
      self.jobsDescription = []
      _item1 = None
      _jobsDescriptionLen = input.readUnsignedShort()
      for _i1 in range(0,_jobsDescriptionLen):
         _item1 = JobDescription(input)
         self.jobsDescription.append(_item1)