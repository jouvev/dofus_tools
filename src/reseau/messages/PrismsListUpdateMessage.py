from src.reseau.messages.PrismsListMessage import PrismsListMessage

class PrismsListUpdateMessage(PrismsListMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
