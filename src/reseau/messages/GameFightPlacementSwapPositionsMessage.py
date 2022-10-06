from src.reseau.types.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations

class GameFightPlacementSwapPositionsMessage:
   def __init__(self,input):
      for _i1 in range(0,2):
         self.dispositions[_i1] = IdentifiedEntityDispositionInformations(input)

   def resume(self):
      pass