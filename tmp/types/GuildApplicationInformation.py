from tmp.types.ApplicationPlayerInformation import ApplicationPlayerInformation

class GuildApplicationInformation:
   def __init__(self,input):
      self.playerInfo = ApplicationPlayerInformation(input)
      self._applyTextFunc(input)
      self._creationDateFunc(input)
   
   def _applyTextFunc(self,input) :
      self.applyText = input.readUTF()
   
   def _creationDateFunc(self,input) :
      self.creationDate = input.readDouble()
      if(self.creationDate < -9007199254740992 or self.creationDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.creationDate) + ") on element of GuildApplicationInformation.creationDate.")

   def resume(self):
      print("applyText :",self.applyText)
      print("creationDate :",self.creationDate)
      self.playerInfo.resum()
