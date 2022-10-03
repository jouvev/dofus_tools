from tmp.messages.CharacterReplayRequestMessage import CharacterReplayRequestMessage
from tmp.types.RemodelingInformation import RemodelingInformation
class CharacterReplayWithRemodelRequestMessage(CharacterReplayRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self.remodel = RemodelingInformation(input)