from tmp.types.JobExperience import JobExperience
class JobExperienceUpdateMessage:
   def __init__(self,input):
      self.experiencesUpdate = JobExperience(input)