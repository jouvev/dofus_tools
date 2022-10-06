from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations

class InviteInHavenBagClosedMessage:
   def __init__(self,input):
      self.hostInformations = CharacterMinimalInformations(input)

   def resume(self):
      self.hostInformations.resum()
