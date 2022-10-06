from tmp.messages.CharactersListMessage import CharactersListMessage
from tmp.types.CharacterToRemodelInformations import CharacterToRemodelInformations

class CharactersListWithRemodelingMessage(CharactersListMessage):
   def __init__(self,input):
      self.charactersToRemodel = []
      _item1 = None
      super().__init__(input)
      _charactersToRemodelLen = input.readUnsignedShort()
      for _i1 in range(0,_charactersToRemodelLen):
         _item1 = CharacterToRemodelInformations(input)
         self.charactersToRemodel.append(_item1)

   def resume(self):
      super().resume()
      for e in self.charactersToRemodel:
         e.resume()
