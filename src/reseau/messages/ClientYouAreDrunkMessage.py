from src.reseau.messages.DebugInClientMessage import DebugInClientMessage

class ClientYouAreDrunkMessage(DebugInClientMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
