class GuildApplicationListenMessage:
   def __init__(self,input):
      self._listenFunc(input)
   
   def _listenFunc(self,input) :
      self.listen = input.readBoolean()

   def resume(self):
      print("listen :",self.listen)
