class CharacterCanBeCreatedResultMessage:
   def __init__(self,input):
      self._yesYouCanFunc(input)
   
   def _yesYouCanFunc(self,input) :
      self.yesYouCan = input.readBoolean()