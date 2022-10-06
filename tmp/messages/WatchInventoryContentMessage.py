from tmp.messages.InventoryContentMessage import InventoryContentMessage

class WatchInventoryContentMessage(InventoryContentMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
