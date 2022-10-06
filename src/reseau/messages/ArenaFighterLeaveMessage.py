from src.reseau.types.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations

class ArenaFighterLeaveMessage:
   def __init__(self,input):
      self.leaver = CharacterBasicMinimalInformations(input)

   def resume(self):
      self.leaver.resum()
