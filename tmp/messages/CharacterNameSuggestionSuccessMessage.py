class CharacterNameSuggestionSuccessMessage:
   def __init__(self,input):
      self._suggestionFunc(input)
   
   def _suggestionFunc(self,input) :
      self.suggestion = input.readUTF()

   def resume(self):
      print("suggestion :",self.suggestion)
