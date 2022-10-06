class ExchangeMountFreeFromPaddockMessage:
   def __init__(self,input):
      self._nameFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._liberatorFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of ExchangeMountFreeFromPaddockMessage.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of ExchangeMountFreeFromPaddockMessage.worldY.")
   
   def _liberatorFunc(self,input) :
      self.liberator = input.readUTF()

   def resume(self):
      print("name :",self.name)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("liberator :",self.liberator)
