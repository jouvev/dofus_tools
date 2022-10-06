from src.reseau.types.GuildEmblem import GuildEmblem

class AllianceCreationValidMessage:
   def __init__(self,input):
      self._allianceNameFunc(input)
      self._allianceTagFunc(input)
      self.allianceEmblem = GuildEmblem(input)
   
   def _allianceNameFunc(self,input) :
      self.allianceName = input.readUTF()
   
   def _allianceTagFunc(self,input) :
      self.allianceTag = input.readUTF()

   def resume(self):
      print("allianceName :",self.allianceName)
      print("allianceTag :",self.allianceTag)
      self.allianceEmblem.resum()
