from tmp.types.PaddockContentInformations import PaddockContentInformations

class GuildPaddockBoughtMessage:
   def __init__(self,input):
      self.paddockInfo = PaddockContentInformations(input)

   def resume(self):
      self.paddockInfo.resum()
