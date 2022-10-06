class PaddockInformationsForSell:
   def __init__(self,input):
      self._guildOwnerFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._subAreaIdFunc(input)
      self._nbMountFunc(input)
      self._nbObjectFunc(input)
      self._priceFunc(input)
   
   def _guildOwnerFunc(self,input) :
      self.guildOwner = input.readUTF()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PaddockInformationsForSell.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PaddockInformationsForSell.worldY.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PaddockInformationsForSell.subAreaId.")
   
   def _nbMountFunc(self,input) :
      self.nbMount = input.readByte()
   
   def _nbObjectFunc(self,input) :
      self.nbObject = input.readByte()
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of PaddockInformationsForSell.price.")

   def resume(self):
      print("guildOwner :",self.guildOwner)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("subAreaId :",self.subAreaId)
      print("nbMount :",self.nbMount)
      print("nbObject :",self.nbObject)
      print("price :",self.price)
