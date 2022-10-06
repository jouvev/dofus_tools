import tmp.TypesFactory as pf
from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightDispellableEffectMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.effect = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      super().resume()
