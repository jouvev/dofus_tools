from src.reseau.types.JobExperience import JobExperience

class JobExperienceUpdateMessage:
   def __init__(self,input):
      self.experiencesUpdate = JobExperience(input)

   def resume(self):
      self.experiencesUpdate.resum()
