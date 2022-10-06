from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations

class InviteInHavenBagMessage:
   def __init__(self,input):
      self.guestInformations = CharacterMinimalInformations(input)
      self._acceptFunc(input)
   
   def _acceptFunc(self,input) :
      self.accept = input.readBoolean()

   def resume(self):
      print("accept :",self.accept)
      self.guestInformations.resum()
