from src.reseau.messages.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage

class TopTaxCollectorListMessage(AbstractTaxCollectorListMessage):
   def __init__(self,input):
      super().__init__(input)
      self._isDungeonFunc(input)
   
   def _isDungeonFunc(self,input) :
      self.isDungeon = input.readBoolean()

   def resume(self):
      super().resume()
      print("isDungeon :",self.isDungeon)
