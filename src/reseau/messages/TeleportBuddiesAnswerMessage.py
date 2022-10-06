class TeleportBuddiesAnswerMessage:
   def __init__(self,input):
      self._acceptFunc(input)
   
   def _acceptFunc(self,input) :
      self.accept = input.readBoolean()

   def resume(self):
      print("accept :",self.accept)
