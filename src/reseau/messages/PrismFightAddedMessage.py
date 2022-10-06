from src.reseau.types.PrismFightersInformation import PrismFightersInformation

class PrismFightAddedMessage:
   def __init__(self,input):
      self.fight = PrismFightersInformation(input)

   def resume(self):
      self.fight.resum()
