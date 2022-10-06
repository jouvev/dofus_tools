class ExchangeMountsTakenFromPaddockMessage:
   def __init__(self,input):
      self._nameFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._ownernameFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of ExchangeMountsTakenFromPaddockMessage.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of ExchangeMountsTakenFromPaddockMessage.worldY.")
   
   def _ownernameFunc(self,input) :
      self.ownername = input.readUTF()

   def resume(self):
      print("name :",self.name)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("ownername :",self.ownername)
