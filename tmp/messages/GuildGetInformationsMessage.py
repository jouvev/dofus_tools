class GuildGetInformationsMessage:
   def __init__(self,input):
      self._infoTypeFunc(input)
   
   def _infoTypeFunc(self,input) :
      self.infoType = input.readByte()
      if(self.infoType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.infoType) + ") on element of GuildGetInformationsMessage.infoType.")

   def resume(self):
      print("infoType :",self.infoType)
