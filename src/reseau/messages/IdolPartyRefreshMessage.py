from src.reseau.types.PartyIdol import PartyIdol

class IdolPartyRefreshMessage:
   def __init__(self,input):
      self.partyIdol = PartyIdol(input)

   def resume(self):
      self.partyIdol.resume()
