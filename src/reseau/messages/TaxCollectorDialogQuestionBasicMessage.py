from src.reseau.types.BasicGuildInformations import BasicGuildInformations

class TaxCollectorDialogQuestionBasicMessage:
   def __init__(self,input):
      self.guildInfo = BasicGuildInformations(input)

   def resume(self):
      self.guildInfo.resum()
