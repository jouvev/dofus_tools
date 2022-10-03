class CharacterCapabilitiesMessage:
   def __init__(self,input):
      self._guildEmblemSymbolCategoriesFunc(input)
   
   def _guildEmblemSymbolCategoriesFunc(self,input) :
      self.guildEmblemSymbolCategories = input.readVarUhInt()
      if(self.guildEmblemSymbolCategories < 0) :
         raise RuntimeError("Forbidden value (" + self.guildEmblemSymbolCategories + ") on element of CharacterCapabilitiesMessage.guildEmblemSymbolCategories.")