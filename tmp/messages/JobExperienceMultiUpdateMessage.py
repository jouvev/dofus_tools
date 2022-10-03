from tmp.types.JobExperience import JobExperience
class JobExperienceMultiUpdateMessage:
   def __init__(self,input):
      self.experiencesUpdate = []
      _item1 = None
      _experiencesUpdateLen = input.readUnsignedShort()
      for _i1 in range(0,_experiencesUpdateLen):
         _item1 = JobExperience(input)
         self.experiencesUpdate.append(_item1)