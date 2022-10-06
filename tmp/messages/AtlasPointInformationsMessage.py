from tmp.types.AtlasPointsInformations import AtlasPointsInformations

class AtlasPointInformationsMessage:
   def __init__(self,input):
      self.type = AtlasPointsInformations(input)

   def resume(self):
      self.type.resum()
