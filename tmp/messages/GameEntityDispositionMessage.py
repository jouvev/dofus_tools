from tmp.types.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
class GameEntityDispositionMessage:
   def __init__(self,input):
      self.disposition = IdentifiedEntityDispositionInformations(input)