from src.reseau.messages.AbstractGameActionMessage import AbstractGameActionMessage
from src.reseau.types.GameActionMark import GameActionMark

class GameActionFightMarkCellsMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self.mark = GameActionMark(input)

   def resume(self):
      super().resume()
      self.mark.resume()
