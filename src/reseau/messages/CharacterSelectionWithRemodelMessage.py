from src.reseau.messages.CharacterSelectionMessage import CharacterSelectionMessage
from src.reseau.types.RemodelingInformation import RemodelingInformation

class CharacterSelectionWithRemodelMessage(CharacterSelectionMessage):
   def __init__(self,input):
      super().__init__(input)
      self.remodel = RemodelingInformation(input)

   def resume(self):
      super().resume()
      self.remodel.resume()
