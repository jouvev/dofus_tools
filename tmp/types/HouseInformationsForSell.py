from tmp.types.AccountTagInformation import AccountTagInformation

class HouseInformationsForSell:
   def __init__(self,input):
      self.skillListIds = []
      _val12 = 0
      self._instanceIdFunc(input)
      self._secondHandFunc(input)
      self._modelIdFunc(input)
      self.ownerTag = AccountTagInformation(input)
      self._hasOwnerFunc(input)
      self._ownerCharacterNameFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._subAreaIdFunc(input)
      self._nbRoomFunc(input)
      self._nbChestFunc(input)
      _skillListIdsLen = input.readUnsignedShort()
      for _i12 in range(0,_skillListIdsLen):
         _val12 = input.readInt()
         self.skillListIds.append(_val12)
      self._isLockedFunc(input)
      self._priceFunc(input)
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseInformationsForSell.instanceId.")
   
   def _secondHandFunc(self,input) :
      self.secondHand = input.readBoolean()
   
   def _modelIdFunc(self,input) :
      self.modelId = input.readVarUhInt()
      if(self.modelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of HouseInformationsForSell.modelId.")
   
   def _hasOwnerFunc(self,input) :
      self.hasOwner = input.readBoolean()
   
   def _ownerCharacterNameFunc(self,input) :
      self.ownerCharacterName = input.readUTF()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of HouseInformationsForSell.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of HouseInformationsForSell.worldY.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of HouseInformationsForSell.subAreaId.")
   
   def _nbRoomFunc(self,input) :
      self.nbRoom = input.readByte()
   
   def _nbChestFunc(self,input) :
      self.nbChest = input.readByte()
   
   def _isLockedFunc(self,input) :
      self.isLocked = input.readBoolean()
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of HouseInformationsForSell.price.")

   def resume(self):
      print("instanceId :",self.instanceId)
      print("secondHand :",self.secondHand)
      print("modelId :",self.modelId)
      print("hasOwner :",self.hasOwner)
      print("ownerCharacterName :",self.ownerCharacterName)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("subAreaId :",self.subAreaId)
      print("nbRoom :",self.nbRoom)
      print("nbChest :",self.nbChest)
      print("isLocked :",self.isLocked)
      print("price :",self.price)
      self.ownerTag.resum()
      print("skillListIds :",self.skillListIds)
