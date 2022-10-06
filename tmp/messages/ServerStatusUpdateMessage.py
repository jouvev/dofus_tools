from tmp.types.GameServerInformations import GameServerInformations

class ServerStatusUpdateMessage:
   def __init__(self,input):
      self.server = GameServerInformations(input)

   def resume(self):
      self.server.resum()
