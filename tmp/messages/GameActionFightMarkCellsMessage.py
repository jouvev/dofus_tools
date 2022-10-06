from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage
from tmp.types.GameActionMark import GameActionMark

class GameActionFightMarkCellsMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self.mark = GameActionMark(input)

   def resume(self):
      super().resume()
      self.mark.resum()
