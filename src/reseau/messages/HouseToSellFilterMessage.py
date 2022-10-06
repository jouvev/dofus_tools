class HouseToSellFilterMessage:
   def __init__(self,input):
      self._areaIdFunc(input)
      self._atLeastNbRoomFunc(input)
      self._atLeastNbChestFunc(input)
      self._skillRequestedFunc(input)
      self._maxPriceFunc(input)
      self._orderByFunc(input)
   
   def _areaIdFunc(self,input) :
      self.areaId = input.readInt()
   
   def _atLeastNbRoomFunc(self,input) :
      self.atLeastNbRoom = input.readByte()
      if(self.atLeastNbRoom < 0) :
         raise RuntimeError("Forbidden value (" + str(self.atLeastNbRoom) + ") on element of HouseToSellFilterMessage.atLeastNbRoom.")
   
   def _atLeastNbChestFunc(self,input) :
      self.atLeastNbChest = input.readByte()
      if(self.atLeastNbChest < 0) :
         raise RuntimeError("Forbidden value (" + str(self.atLeastNbChest) + ") on element of HouseToSellFilterMessage.atLeastNbChest.")
   
   def _skillRequestedFunc(self,input) :
      self.skillRequested = input.readVarUhShort()
      if(self.skillRequested < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillRequested) + ") on element of HouseToSellFilterMessage.skillRequested.")
   
   def _maxPriceFunc(self,input) :
      self.maxPrice = input.readVarUhLong()
      if(self.maxPrice < 0 or self.maxPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.maxPrice) + ") on element of HouseToSellFilterMessage.maxPrice.")
   
   def _orderByFunc(self,input) :
      self.orderBy = input.readByte()
      if(self.orderBy < 0) :
         raise RuntimeError("Forbidden value (" + str(self.orderBy) + ") on element of HouseToSellFilterMessage.orderBy.")

   def resume(self):
      print("areaId :",self.areaId)
      print("atLeastNbRoom :",self.atLeastNbRoom)
      print("atLeastNbChest :",self.atLeastNbChest)
      print("skillRequested :",self.skillRequested)
      print("maxPrice :",self.maxPrice)
      print("orderBy :",self.orderBy)
