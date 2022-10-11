from src.reseau.messages.CharacterReplayRequestMessage import CharacterReplayRequestMessage
from src.reseau.types.RemodelingInformation import RemodelingInformation

class CharacterReplayWithRemodelRequestMessage(CharacterReplayRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self.remodel = RemodelingInformation(input)

   def resume(self):
      super().resume()
      self.remodel.resume()
