import tmp.TypesFactory as pf

class JobDescription:
   def __init__(self,input):
      self.skills = []
      _id2 = 0
      _item2 = None
      self._jobIdFunc(input)
      _skillsLen = input.readUnsignedShort()
      for _i2 in range(0,_skillsLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.skills.append(_item2)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobDescription.jobId.")

   def resume(self):
      print("jobId :",self.jobId)
      for e in self.skills:
         e.resume()
