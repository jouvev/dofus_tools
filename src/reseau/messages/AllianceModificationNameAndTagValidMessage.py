class AllianceModificationNameAndTagValidMessage:
   def __init__(self,input):
      self._allianceNameFunc(input)
      self._allianceTagFunc(input)
   
   def _allianceNameFunc(self,input) :
      self.allianceName = input.readUTF()
   
   def _allianceTagFunc(self,input) :
      self.allianceTag = input.readUTF()

   def resume(self):
      print("allianceName :",self.allianceName)
      print("allianceTag :",self.allianceTag)
