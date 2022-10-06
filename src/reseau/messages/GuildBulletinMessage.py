from src.reseau.messages.BulletinMessage import BulletinMessage

class GuildBulletinMessage(BulletinMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
