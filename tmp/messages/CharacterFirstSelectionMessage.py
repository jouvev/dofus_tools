from tmp.messages.CharacterSelectionMessage import CharacterSelectionMessage
class CharacterFirstSelectionMessage(CharacterSelectionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._doTutorialFunc(input)
   
   def _doTutorialFunc(self,input) :
      self.doTutorial = input.readBoolean()