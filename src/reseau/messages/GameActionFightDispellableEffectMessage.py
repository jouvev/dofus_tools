import src.reseau.TypesFactory as pf
from src.reseau.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightDispellableEffectMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.effect = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      super().resume()
      self.effect.resume()
