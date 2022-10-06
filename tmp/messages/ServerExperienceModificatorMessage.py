class ServerExperienceModificatorMessage:
   def __init__(self,input):
      self._experiencePercentFunc(input)
   
   def _experiencePercentFunc(self,input) :
      self.experiencePercent = input.readVarUhShort()
      if(self.experiencePercent < 0) :
         raise RuntimeError("Forbidden value (" + str(self.experiencePercent) + ") on element of ServerExperienceModificatorMessage.experiencePercent.")

   def resume(self):
      print("experiencePercent :",self.experiencePercent)
