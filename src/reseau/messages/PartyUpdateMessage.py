import src.reseau.TypesFactory as pf
from src.reseau.messages.AbstractPartyEventMessage import AbstractPartyEventMessage

class PartyUpdateMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.memberInformations = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      super().resume()
