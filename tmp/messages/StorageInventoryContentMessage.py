from tmp.messages.InventoryContentMessage import InventoryContentMessage

class StorageInventoryContentMessage(InventoryContentMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
