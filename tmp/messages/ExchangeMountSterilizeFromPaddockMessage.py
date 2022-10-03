class ExchangeMountSterilizeFromPaddockMessage:
   def __init__(self,input):
      self._nameFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._sterilizatorFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + self.worldX + ") on element of ExchangeMountSterilizeFromPaddockMessage.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + self.worldY + ") on element of ExchangeMountSterilizeFromPaddockMessage.worldY.")
   
   def _sterilizatorFunc(self,input) :
      self.sterilizator = input.readUTF()