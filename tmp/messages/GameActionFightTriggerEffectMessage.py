from tmp.messages.GameActionFightDispellEffectMessage import GameActionFightDispellEffectMessage

class GameActionFightTriggerEffectMessage(GameActionFightDispellEffectMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
