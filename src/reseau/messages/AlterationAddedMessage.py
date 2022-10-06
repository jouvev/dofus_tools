from src.reseau.types.AlterationInfo import AlterationInfo

class AlterationAddedMessage:
   def __init__(self,input):
      self.alteration = AlterationInfo(input)

   def resume(self):
      self.alteration.resum()
