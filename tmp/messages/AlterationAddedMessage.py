from tmp.types.AlterationInfo import AlterationInfo
class AlterationAddedMessage:
   def __init__(self,input):
      self.alteration = AlterationInfo(input)