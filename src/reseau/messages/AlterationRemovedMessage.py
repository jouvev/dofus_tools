from src.reseau.types.AlterationInfo import AlterationInfo

class AlterationRemovedMessage:
   def __init__(self,input):
      self.alteration = AlterationInfo(input)

   def resume(self):
      self.alteration.resume()
