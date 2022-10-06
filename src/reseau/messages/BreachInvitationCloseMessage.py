from src.reseau.types.CharacterMinimalInformations import CharacterMinimalInformations

class BreachInvitationCloseMessage:
   def __init__(self,input):
      self.host = CharacterMinimalInformations(input)

   def resume(self):
      self.host.resum()
